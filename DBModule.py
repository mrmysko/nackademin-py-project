import sqlite3

from ExtractData import ExtractData
from Product import Product


class Database:
    """Creates an SQLite-database object"""

    def __init__(self, file):
        self.file = file

        # Open a connection to the database.
        self.connection = sqlite3.connect(file)

        # Open a cursor to the database.
        self.cursor = self.connection.cursor()

        # Create table if it doesnt exist. - This is supposed to get time data from python, but SQLite supports its own datetime.
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS products( 
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    price TEXT, 
                    url TEXT NOT NULL,
                    last_updated TEXT,
                    lowest_price INTEGER,
                    lowest_price_date TEXT
                    ) STRICT"""
        )

        # Commit the command to db.
        self.connection.commit()

        # Get columns in db
        self.cursor.execute("SELECT * FROM products")
        self.columns = [col[0] for col in self.cursor.description]

    def get_product_data(self, id) -> Product:
        """returns a single row of "id" product data."""

        data = self.cursor.execute("SELECT * FROM products WHERE id = ?", (id,))

        return self.define_products(data)[0]

    def insert_product_data(self, product: Product) -> int:
        """inserts data into the database."""

        self.cursor.execute(
            "INSERT INTO products ('name', 'price', 'url', 'last_updated', 'lowest_price', 'lowest_price_date') VALUES (?, ?, ?, ?, ?, ?)",
            product.__data__(),
        )

        self.connection.commit()
        return self.cursor.rowcount

    def remove_product_data(self, product) -> bool:
        """removes items from the database."""

        if self.cursor.execute("DELETE FROM products WHERE id = ?", (product.id,)):
            self.connection.commit()
            return True

    def update_product_data(self, product: Product):
        """updates a products data."""

        update_tuple = (
            product.name,
            product.price,
            product.last_updated,
            product.lowest_price,
            product.lowest_price_date,
            product.url,
        )

        self.cursor.execute(
            f"UPDATE products SET name = ?, price = ?, last_updated = ?, lowest_price = ?, lowest_price_date = ? WHERE url = ?",
            update_tuple,
        )

        self.connection.commit()

    def dump_db(self) -> list:
        """returns a list of product class-objects."""

        # Get all rows from database.
        all_rows = self.cursor.execute("SELECT * FROM products")

        return self.define_products(all_rows)

    def search_db(self, search_term) -> list:
        """search name column for strings matching search_term"""

        matching_rows = self.cursor.execute(
            "SELECT * FROM products WHERE name LIKE ?",
            ("%" + search_term + "%",),
        )

        return self.define_products(matching_rows)

    def define_products(self, cursor_obj) -> list:
        """creates product objects from rows in a given cursor object"""

        # List to store zip objects with col, value tuples.
        tupled_values = []

        # Creates a list of zip objects consisting of col, value pairs.
        """printing tupled_values gives [zip-object, zip-object, zip-object...]
        And printing tupled_values[0] gives [("id", 1), ("name", "something"), ("price", "100")] etc
        So each list element in tuple_rows contains a list of all zipped values."""
        for row in cursor_obj:
            tupled_values.append(zip(self.columns, row))

        # Creates product objects for every zipped value, the star in the argument unpacks zip and passes tuples as arguments.
        products = [Product(*row) for row in tupled_values]

        # This is a list of class-objects.
        return products

    def close_db(self):
        """closes the database connection."""

        self.cursor.close()
        self.connection.close()
