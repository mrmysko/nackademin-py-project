# Notes:
# Selenium verkar onödigt stort, en hel webbläsarmotor för en request.
# Webhallen anävnder ett js för att generera typ hela deras webbsida, pivot till netonnet KEKL

from bs4 import BeautifulSoup
import requests


class Product:
    def __init__(self, name, price, url):
        self.name = name
        self.price = price
        self.url = url

    def update_price(self, url):

        # get_shop(url)

        self.price = "some_price"


# Sets the headers for use with beatifulsoup, server does not allow requests without a normal header?
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

# Asks for a url, extract name and price and print to console.
url = input("URL: ")
# url = "https://www.netonnet.se/art/dator-surfplatta/laptop/chromebook/hp-chromebook-cx14a-ca0003-hc4120464mch/1028611.16492/"

# Requested url to get, with headers as argument. Returns a request-object.
site_content = requests.get(url, headers=headers)

# Instantiates a bs-object with request-content and lxml as parser.
soup = BeautifulSoup(site_content.content, "lxml")

# Extracts the name of the product.
name = soup.find("div", {"class": "subTitle big"}).get_text().strip()
print(name)

# Selects the div with classname "price-big", gets the text inside the div and strips it of whitespace. Prints as e.g. "2 990:-"
price = soup.find("div", {"class": "price-big"}).get_text().strip()

print(price)

product = Product(name, price, url)
