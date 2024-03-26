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

    # Selects the div with classname "price-big", gets the text inside the div and strips it of whitespace. Prints as e.g. "2 990:-" - Should prolly remove ":-" and convert this to a int.
    price = soup.find("div", {"class": "price-big"}).get_text().strip()

    return (name, price)
