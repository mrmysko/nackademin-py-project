class Product:
    def __init__(
        self,
        id,
        name,
        price,
        url,
        last_updated,
        lowest_price=None,
        lowest_price_date=None,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.url = url
        self.last_updated = last_updated
        self.lowest_price = lowest_price
        self.lowest_price_date = lowest_price_date

        if lowest_price == None:
            self.lowest_price = self.price
            self.lowest_price_date = self.last_updated

    def __str__(self):
        return self.name

    def __data__(self):
        """this is just to pass a class-objekt in a format the db can parse."""

        return (
            self.name,
            str(self.price),
            self.url,
            self.last_updated,
            self.lowest_price,
            self.lowest_price_date,
        )

    def update_date(self):
        pass
