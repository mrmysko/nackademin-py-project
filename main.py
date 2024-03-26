# Notes:
# Selenium verkar onödigt stort, en hel webbläsarmotor för en request.
# Webhallen anävnder ett js för att generera typ hela deras webbsida, pivot till netonnet KEKL

# bs4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# sqlite3
# https://docs.python.org/3/library/sqlite3.html

import os

from ExtractData import ExtractData
from DBModule import Database
from Product import Product


db = Database("price.db")


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)


while True:
    clear_console()

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")
    print("1. Query item.")
    print("2. Add item.")
    print("3. Dump DB.")
    print("e. Exit")
    # print("1. Add item.")
    # print("2. Del item.")
    # print("3. Query DB.")

    user_choice = input(": ")

    if user_choice == "1":

        url = input("URL: ")
        name, price = ExtractData(url)

        product = Product(name, price, url)

        print(name)
        print(price)
        print(url)
        input()

    elif user_choice == "2":
        db.insert_product_data((product.name, product.price, product.url))

    elif user_choice == "3":
        print(db.dump_db())
        input()

    elif user_choice.lower() == "e":
        break
# name, price = ExtractData(url)
# product = Product(name, price, url)

# print(product.name)
# print(product.price)
# print(product.url)
