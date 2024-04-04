class Product:
    """creates a product object"""

    def __init__(self, *args):
        """initialize a product object."""

        # Unpacks and dynamically assigns variables.
        for attr, value in args:
            setattr(self, attr, value)

        if not hasattr(self, "lowest_price"):
            self.lowest_price = self.price
            self.lowest_price_date = self.last_updated

    def __str__(self):
        return self.name


if __name__ == "__main__":
    pass
