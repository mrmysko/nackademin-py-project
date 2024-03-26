import sqlite3

# Kan en db vara ett klassobjekt?


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

    def dump_db(self):
        return self.cur.execute("SELECT * FROM products").fetchall()
