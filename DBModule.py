import sqlite3

# Att man använder placeholders (?) istället för string format har tydligen med att preventa SQL-injections att göra.

# Use with statements to close db-connection and cursor when done.


class Database:
    """Creates an SQLite-database object"""

    def __init__(self, file):
        self.file = file

        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS products( 
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    price TEXT, 
                    url TEXT NOT NULL
                    ) STRICT"""
        )

        self.con.commit()

    def insert_product_data(self, data: tuple):

        self.cur.execute(
            f"INSERT INTO products ('name', 'price', 'url') VALUES (?, ?, ?)", data
        )

        self.con.commit()

    def remove_product_data(self, id):
        # Add confirmation. - BUT, I dont even know if I want the print and confirmation here...thats user facing stuff, only place database methods here.
        # Do something like, Query for id -> Get that data and display it -> Ask for confirmation -> remove_product_data(id)
        self.cur.execute("DELETE FROM products WHERE id = ?", id)
        self.con.commit()
        print(self.cur.rowcount, "record(s) deleted")
        input()

    def print_db(self):

        longest_name = 0
        for id_, name, price_, url_ in self.dump_db():
            if len(name) > longest_name:
                longest_name = len(name)

        for id, name, price, url in self.dump_db():
            print(
                f"{str(id).rjust(3)} {name.rjust(longest_name)} {price.rjust(0)} {url.rjust(0)}"
            )

    def dump_db(self):
        return self.cur.execute("SELECT * FROM products").fetchall()
