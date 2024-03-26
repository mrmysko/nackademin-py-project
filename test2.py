# Webhallen anävnder ett js för att generera typ hela deras webbsida, pivot till netonnet KEKL

from bs4 import BeautifulSoup
import requests


# Sets the headers for use with beatifulsoup, server does not allow requests without a normal header?
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

# Requested url to get, with headers as argument. Returns a request-object.
site = requests.get(
    "https://www.netonnet.se/art/dator-surfplatta/laptop/chromebook/hp-chromebook-cx14a-ca0003-hc4120464mch/1028611.16492/",
    headers=headers,
)

# Instantiates a bs-object with request-content and lxml as parser.
soup = BeautifulSoup(site.content, "lxml")

print(type(soup))


name = soup.find("h1")
print(name)

# Selects the div with classname "price-big", gets the text inside the div and strips it of whitespace. Prints as e.g. "2 990:-"
price = soup.find("div", {"class": "price-big"}).get_text().strip()

print(price)
