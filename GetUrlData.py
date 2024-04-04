import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_url_data(url: str) -> tuple:
    """extracts name and price data of a given netonnet URL"""

    # Netonnet didnt like requests without a useragent.
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    }

    try:
        # Requested url to get, with headers as argument. Returns a request-object.
        site = requests.get(url, headers=headers)
        site.raise_for_status()
    except requests.exceptions.RequestException:
        raise

    # Instantiates a bs-object with request-content and lxml as parser.
    soup = BeautifulSoup(site.content, "lxml")

    try:
        # Extracts name and price.
        breadcrumb = soup.find("ol", {"class": "breadcrumb"})
        name = breadcrumb.find("span").get_text(strip=True)
        price = soup.find("div", {"class": "price-big"}).get_text(strip=True)

    except AttributeError:
        raise

    # Removes ":-" from price and converts to an int.
    # Has to be a cleaner way to do this.
    price = re.sub(":-$", "", price)
    price = "".join(price.split()).strip()
    price = int(price)

    last_updated = datetime.now().isoformat()

    return (
        ("name", name),
        ("price", price),
        ("url", url),
        ("last_updated", last_updated),
    )
