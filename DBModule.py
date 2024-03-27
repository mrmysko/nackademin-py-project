import sqlite3

from ExtractData import ExtractData

# Att man använder placeholders (?) istället för string format har tydligen med att preventa SQL-injections att göra.

# Use with statements to close db-connection and cursor when done.


class Database:
    """Creates an SQLite-database object"""

    def __init__(self, file):
        self.file = file

        # Open a connection to the database.
        self.connection = sqlite3.connect(file)

        # Open a cursor to the database.
        self.cursor = self.connection.cursor()

        # Create table if it doesnt exist.
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS products( 
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    price TEXT, 
                    url TEXT NOT NULL
                    ) STRICT"""
        )

        # Commit the command to db.
        self.connection.commit()

    def insert_product_data(self, data: tuple):
        """Inserts data into the database."""

        self.cursor.execute(
            "INSERT INTO products ('name', 'price', 'url') VALUES (?, ?, ?)", data
        )

        self.connection.commit()
        return self.cursor.rowcount

    def remove_product_data(self, id) -> int:
        """Removes items from the database."""

        self.cursor.execute("DELETE FROM products WHERE id = ?", id)
        self.connection.commit()
        return self.cursor.rowcount

    def get_product_data(self, id) -> tuple:
        """Returns a single row of "id" product data."""

        return self.cursor.execute("SELECT * FROM products WHERE id = ?", id).fetchone()

    def update_product_data(self, id) -> int:
        """Retrieves updated product data from "id"s url."""

        url = self.cursor.execute(
            "SELECT url FROM products WHERE id = ?", id
        ).fetchone()[0]

        self.cursor.execute(
            "UPDATE products SET name = ?, price = ? WHERE url = ?", ExtractData(url)
        )

        self.connection.commit()

        return self.cursor.rowcount

    def dump_db(self) -> list:
        """Returns entire database as a list of tuples."""

        return self.cursor.execute("SELECT * FROM products").fetchall()

    def search_db(self, search_term):
        """Search all (not timestamp) columns for strings matching search_term"""

        return self.cursor.execute(
            "SELECT * FROM products WHERE name LIKE ?",
            ("%" + search_term + "%",),
        ).fetchall()
