import sqlite3

from Product import Product


class Database:
    """creates an SQLite-database object"""

    def __init__(self, file):
        self.file = file

        self.connection = sqlite3.connect(self.file)

        self.cursor = self.connection.cursor()

        # Create table if it doesnt exist.
        # This is supposed to get time data from python, but SQLite supports its own datetime. Find out how.
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS products( 
                    id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    price INTEGER, 
                    url TEXT NOT NULL,
                    last_updated TEXT,
                    lowest_price INTEGER,
                    lowest_price_date TEXT
                    ) STRICT"""
        )

        self.connection.commit()

        # Get columns in db
        self.cursor.execute("SELECT * FROM products")
        self.columns = [col[0] for col in self.cursor.description]

    def get_product_data(self, id) -> Product:
        """returns a product object of ids database data.

        Will instead return False if the id was not found."""

        data = self.cursor.execute("SELECT * FROM products WHERE id = ?", (id,))

        # Problemet här är att efter if not list(data) har kollat om listan är tom så
        # discardar cursor-objectet den raden.
        # Flowet här går typ:
        #       Skaffa cursor-object ->
        #       Kolla om det är tomt. ->
        #       Om det inte är det, skicka det till define_products. ->
        #       Men om det bara va en rad i objectet så är cursorn tom nu.
        # Alternativt att använda .fetchall()/one() för att stoppa resultatet i minnet och skriva om define_products.

        if not list(data):
            return False

        else:
            # Need to rerun the query to get a "non-discarded" cursor-object.
            data = self.cursor.execute("SELECT * FROM products WHERE id = ?", (id,))

            return self.define_products(data)[0]

    def insert_product_data(self, product: Product) -> int:
        """inserts data into the database."""

        self.cursor.execute(
            "INSERT OR REPLACE INTO products ('id', 'name', 'price', 'url', 'last_updated', 'lowest_price', 'lowest_price_date') VALUES ((SELECT id FROM products WHERE url = ?), ?, ?, ?, ?, ?, ?)",
            (
                product.url,
                product.name,
                product.price,
                product.url,
                product.last_updated,
                product.lowest_price,
                product.lowest_price_date,
            ),
        )

        self.connection.commit()
        return self.cursor.rowcount

    def remove_product_data(self, product) -> int:
        """removes items from the database."""

        self.cursor.execute("DELETE FROM products WHERE id = ?", (product.id,))

        # Not commiting remove until user closes program.
        # self.connection.commit()
        return self.cursor.rowcount

    def dump(self) -> list:
        """returns a list of product class-objects."""

        # Get all rows from database.
        all_rows = self.cursor.execute("SELECT * FROM products")

        return self.define_products(all_rows)

    def search(self, search_term) -> list:
        """search name column for strings matching search_term"""

        matching_rows = self.cursor.execute(
            "SELECT * FROM products WHERE name LIKE ?",
            ("%" + search_term + "%",),
        )

        return self.define_products(matching_rows)

    def define_products(self, cursor_obj) -> list:
        """creates product objects from rows in a given cursor object"""

        # Zips together db.columns and rows into a list of zip objects.
        tupled_values = [zip(self.columns, values) for values in cursor_obj]

        # Creates product objects for every zipped value, the star in the argument unpacks zip and passes tuples as arguments.
        products = [Product(*row) for row in tupled_values]

        # This is a list of class-objects.
        return products

    def close(self):
        """closes the database connection."""

        self.connection.commit()
        self.cursor.close()
        self.connection.close()
