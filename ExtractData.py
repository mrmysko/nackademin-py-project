# Sets the headers for use with beatifulsoup, server does not allow requests without a normal header?
import re
import requests

from datetime import datetime
from bs4 import BeautifulSoup


def ExtractData(url: str) -> tuple:
    """Extracts name and price data of a given netonnet URL"""

    # Netonnet didnt like requests without a useragent.
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    }

    # Requested url to get, with headers as argument. Returns a request-object.
    site_content = requests.get(url, headers=headers)

    # Instantiates a bs-object with request-content and lxml as parser.
    soup = BeautifulSoup(site_content.content, "lxml")

    # Extracts name and price.
    breadcrumb = soup.find("ol", {"class": "breadcrumb"})
    name = breadcrumb.find("span").get_text(strip=True)

    price = soup.find("div", {"class": "price-big"}).get_text(strip=True)

    # Remove art nr from name.
    name = re.sub(" Art.nr:.*$", "", name).strip()

    # Removes ":-" from price and converts to an int.
    # Although, when I display it later I want ":-", but it's easier to work with an int for comparison etc and different stores might display price differently.
    # Has to be a cleaner way to do this.
    price = re.sub(":-$", "", price)
    price = "".join(price.split()).strip()
    price = int(price)

    last_updated = datetime.now().isoformat()

    return (name, price, last_updated)
