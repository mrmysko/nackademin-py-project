"""
A module with helper functions for price-thingy (name pending)
"""

import os
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from Product import Product


def clear_console():
    """
    Clears the console on both windows and unix systems.
    """

    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


def check_update(product: Product) -> tuple:
    """
    Check if a product has updated data, returns three states and the product depending on has updated.\n
    0 - Do nothing, nothing has updated.\n
    1 - Insert updated product in db.\n
    2 - Insert AND mail about lower price.
    """

    try:
        # Creates a new product-object from the supplied products url.
        updated_product = Product(*get_url_data(product.url))
    except requests.exceptions.RequestException:
        raise
    except AttributeError:
        raise

    # If the price of the updated product is the same as the database value. Return False. Mothing has updated.
    if updated_product.price == product.price:
        return (0, product)

    # If the updated price is lower than current, return 2 to mail.
    if updated_product.price < product.price:
        product.price = updated_product.price
        product.last_updated = updated_product.last_updated

        # If the new price is lower, also set the products lowest_price.
        if product.price < product.lowest_price:
            product.lowest_price = product.price
            product.lowest_price_date = product.last_updated

        return (2, product)

    product.price = updated_product.price
    product.last_updated = updated_product.last_updated
    return (1, product)


def get_url_data(url: str) -> tuple:
    """
    Extracts name and price data from a given netonnet URL.
    """

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


def format_message(products: list, alt_format=False) -> str:
    """
    Returns the content of a list of products as a formatted string.
    """

    if not products:
        return "Database empty."

    message = list()
    longest_name = 0

    for product in products:
        if len(product.name) > longest_name:
            longest_name = len(product.name)

        if (
            len(str(product.id))
            + len(product.name)
            + len(str(product.price))
            + len(str(product.lowest_price))
            + len(product.url)
            + 10  # Spaces and vertical lines
        ) > os.get_terminal_size()[0]:
            alt_format = True
            break

    # Alternative formatting
    if alt_format:
        # Multiline f-string looks very ugly...
        for product in products:
            message.append(
                f"""{product.id}.{"-" * 30}
| {product.name}
|  Current Price: {format_price(product.price).rjust(10)}
|   Lowest Price: {format_price(product.lowest_price).rjust(10)}
| {product.url}"""
            )

    else:
        # Cap name at 40 chars.
        if longest_name > 40:
            longest_name = 40

        # Header
        message.append(
            f'{"ID".ljust(2)} | {"NAME".center(longest_name)} | {"CUR PRICE".center(10)} | {"LOW PRICE".rjust(10)} | {"URL".rjust(0)}'
        )

        # Prints db right-justified by longest product name.
        for product in products:
            message.append(
                f"{str(product.id).rjust(2)} | {product.name[:longest_name].rjust(longest_name)} | {format_price(product.price).rjust(10)} | {format_price(product.lowest_price).rjust(10)} | {product.url.rjust(0)}"
            )

    message = "\n".join(message)

    return message


def format_price(price: int) -> str:
    """
    Formats price in a prettier format.
    """

    price = f"{int(price):,} :-".replace(",", " ")

    return price
