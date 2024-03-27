import sqlite3

from ExtractData import ExtractData

# Att man använder placeholders (?) istället för string format har tydligen med att preventa SQL-injections att göra.

# Use with statements to close db-connection and cursor when done.


class Database:
    """Creates an SQLite-database object"""

    def __init__(self, file):
        self.file = file

        # Open a connection to the database.
        self.con = sqlite3.connect(file)

        # Open a cursor to the database.
        self.cur = self.con.cursor()

        # Create table if it doesnt exist.
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS products( 
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    price TEXT, 
                    url TEXT NOT NULL
                    ) STRICT"""
        )

        # Commit the command to db.
        self.con.commit()

    def insert_product_data(self, data: tuple):
        """Inserts data into the database."""

        self.cur.execute(
            "INSERT INTO products ('name', 'price', 'url') VALUES (?, ?, ?)", data
        )

        self.con.commit()
        return self.cur.rowcount

    def remove_product_data(self, id) -> int:
        """Removes items from the database."""

        self.cur.execute("DELETE FROM products WHERE id = ?", id)
        self.con.commit()
        return self.cur.rowcount

    def get_product_data(self, id) -> tuple:
        """Returns a single row of "id" product data."""

        return self.cur.execute("SELECT * FROM products WHERE id = ?", id).fetchone()

    def update_product_data(self, id) -> int:
        """Retrieves updated product data from "id"s url."""

        url = self.cur.execute("SELECT url FROM products WHERE id = ?", id).fetchone()[
            0
        ]

        self.cur.execute(
            "UPDATE products SET name = ?, price = ? WHERE url = ?", ExtractData(url)
        )

        self.con.commit()

        return self.cur.rowcount

    def dump_db(self) -> list:
        """Returns entire database as a list of tuples."""

        return self.cur.execute("SELECT * FROM products").fetchall()
