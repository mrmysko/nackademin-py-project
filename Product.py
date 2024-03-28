class Product:
    def __init__(self, id, name, price, url, last_updated):
        self.id = id
        self.name = name
        self.price = price
        self.url = url
        self.last_updated = last_updated

    def __str__(self):
        return self.name

    def __data__(self):
        """this is just to pass a class-objekt in a format the db can parse."""

        return (self.name, str(self.price), self.url, self.last_updated)
