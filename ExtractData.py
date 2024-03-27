# Sets the headers for use with beatifulsoup, server does not allow requests without a normal header?

from bs4 import BeautifulSoup
import requests
import re


def ExtractData(url: str) -> tuple:
    """Extracts name and price data of a given netonnet URL"""

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    }

    # Requested url to get, with headers as argument. Returns a request-object.
    site_content = requests.get(url, headers=headers)

    # Instantiates a bs-object with request-content and lxml as parser.
    soup = BeautifulSoup(site_content.content, "lxml")

    # Extracts the name of the product. - Should probably format this to remove Art.nr:
    name = soup.find("div", {"class": "subTitle big"}).get_text().strip()

    # Remove art nr from name.
    name = re.sub(" Art.nr: \d*$", "", name)

    # Selects the div with classname "price-big", gets the text inside the div and strips it of whitespace. Prints as e.g. "2 990:-" - Should prolly remove ":-" and convert this to a int.
    price = soup.find("div", {"class": "price-big"}).get_text().strip()

    # Removes ":-" from price and converts to an int.
    # Although, when I display it later I want ":-", but it's easier to work with an int for comparison etc and different stores might display price differently.
    # Has to be a cleaner way to do this.
    price = re.sub(":-$", "", price)
    price = "".join(price.split())

    return (name, price)
