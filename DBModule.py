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

    def get_product_data(self, id) -> Product:
        """returns a single row of "id" product data."""

        data = self.cursor.execute(
            "SELECT * FROM products WHERE id = ?", str(id)
        ).fetchone()

        return Product(*data)

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

        if self.cursor.execute("DELETE FROM products WHERE id = ?", str(product.id)):
            self.connection.commit()
            return True

    def update_product_data(self, product: Product) -> bool:
        """updates a products data."""

        updata = ExtractData(product.url)
        updated = False

        if updata.price < product.price:
            product.price = updata.price
            product.last_updated = updata.last_updated

            updated = True

            update_tuple = (
                product.name,
                product.price,
                product.last_updated,
                product.url,
            )

            self.cursor.execute(
                f"UPDATE products SET name = ?, price = ?, last_updated = ? WHERE url = ?",
                update_tuple,
            )

            self.connection.commit()

        return updated

    def dump_db(self) -> list:
        """returns a list of product class-objects."""

        all_rows = self.cursor.execute("SELECT * FROM products").fetchall()

        products = [Product(*id) for id in all_rows]

        # This is a list of class-objects.
        return products

    def search_db(self, search_term) -> list:
        """search name column for strings matching search_term"""

        matching_rows = self.cursor.execute(
            "SELECT * FROM products WHERE name LIKE ?",
            ("%" + search_term + "%",),
        ).fetchall()

        products = [Product(*id) for id in matching_rows]

        return products

    def update_all(self) -> int:
        """updates all items in the database, returns an int of rows updated."""

        products_updated = 0

        # A second cursor to iterate rows while the first updates them.
        cursor2 = self.connection.cursor()

        cursor2.execute("SELECT * FROM products")
        for row in cursor2:
            if self.update_product_data(Product(*row)):
                products_updated += 1

        cursor2.close()

        return products_updated

    def close_db(self):
        """closes the database connection."""

        self.cursor.close()
        self.connection.close()
