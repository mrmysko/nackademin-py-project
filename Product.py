class Product:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def __str__(self):
        return self.name

    def update_price(self, url):

        # get_shop(url)

        self.price = "some_price"
