from ExtractData import ExtractData


class Product:
    def __init__(self, *args):

        # Unpacks and dynamically assigns variables.
        for attr, value in args:
            setattr(self, attr, value)

        # If this was a call from add_menu the class will only have a self.url.
        # Then call update() to get the info.
        if not hasattr(self, "name"):
            self.update()

    def __str__(self):
        return self.name

    def __data__(self):
        """this is just to pass a class-objekt in a format the db can parse."""

        return (
            self.name,
            self.price,
            self.url,
            self.last_updated,
            self.lowest_price,
            self.lowest_price_date,
        )

    def update(self):
        # This should probably be changed to just update if anything is changed.
        self.name, self.price, self.last_updated = ExtractData(self.url)

        if not hasattr(self, "lowest_price") or self.price < self.lowest_price:
            self.lowest_price = self.price
            self.lowest_price_date = self.last_updated


if __name__ == "__main__":
    pass
