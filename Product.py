from ExtractData import ExtractData


class Product:
    """creates a product object"""

    def __init__(self, *args):
        """initialize a product object."""

        # Unpacks and dynamically assigns variables.
        for attr, value in args:
            setattr(self, attr, value)

        # If this was a call from add_menu the class will only have a self.url.
        # Then call update() to get the info.
        if not hasattr(self, "name"):
            self.update()

    def __str__(self):
        return self.name

    def update(self):
        try:
            self.name, self.price, self.last_updated = ExtractData(self.url)

        # If there's an error here, just raise it to the function that called this.
        except:
            raise

        if not hasattr(self, "lowest_price"):
            self.lowest_price = self.price
            self.lowest_price_date = self.last_updated

        return self


if __name__ == "__main__":
    pass
