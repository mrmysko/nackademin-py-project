import os
import argparse
import time
import requests

from pathlib import Path
from Product import Product
from Database import Database
from concurrent.futures import ThreadPoolExecutor
from FormatMessage import format_message
from MailAlert import mail_alert


# Dont make a static db. Allow to change?
# Opens price.db placed in programs root folder.
# DB_PATH = Path(__file__).with_name("price.db")
DB_PATH = Path(__file__).with_name("edited.db")  # Test-db

DB = Database(DB_PATH)


def clear_console():
    """clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")


def menu_remove():
    """user-facing menu for removing items from database."""

    while True:
        clear_console()

        print("Which item would you like to remove?")
        print("p. Print DB.")
        print("b. Go back.")
        user_choice = input("ID: ")

        # How do I check against both str and int input?
        # 1. input
        # 2. Check if that input CAN become an int with try? - "Bad, only use try for exceptional errors" - Kent
        # 3. If it is an int, do the remove thing?
        # 4. Else: do the match case thing?

        # Hey, thats illegal.
        try:
            int(user_choice)

            product = DB.get_product_data(user_choice)

            if not product:
                input("Index not found.")
                continue

            print(f"Confirm removal of: {product.name}")
            print("(y/n)")

            user_confirm = input(": ")
            match user_confirm.lower():
                case "y":
                    if DB.remove_product_data(product):
                        input(f"{product.name} removed.")
                case _:
                    pass

        except ValueError:
            match user_choice:
                case "p":
                    input(format_message(DB.dump()))
                case "b":
                    break
                case _:
                    pass


def menu_update():
    """user-facing menu for updating database items."""

    while True:
        clear_console()

        print("Which item would you like to update?")
        print("p. Print DB.")
        print("b. Go back.")
        user_choice = input("ID: ")

        # Hey, thats illegal.
        try:
            int(user_choice)

            product = DB.get_product_data(user_choice)

            if not product:
                input("Index not found.")
                continue

            try:
                status, product = check_update(product)
            except requests.exceptions.ConnectionError:
                input("Site unreachable.")
                continue

            # Status 2 in a manual update doesnt require a mail.
            if status == 1 or status == 2:
                if DB.insert_product_data(product):
                    input(f"{product.name} updated.")
                    continue
                else:
                    input("Could not update database.")
                    continue
            input(f"{product.name} already up to date.")

        except ValueError:
            match user_choice:
                case "p":
                    input(format_message(DB.dump()))
                case "b":
                    break
                case _:
                    pass


def menu_add():
    """user-facing menu for adding items to database."""

    clear_console()

    url = input("URL: ")

    try:
        product = Product(("url", url))

        # Check if product is in database, else add it.
        if not DB.insert_product_data(product):
            message = f"Could not add {product.name} to database."
        else:
            message = f"Added {product.name} to database."

    except AttributeError:
        message = "Data not found."
    # Do I really need to import requests just to catch a raised error?
    except requests.exceptions.ConnectionError:
        message = "Site unreachable."

    input(message)


def menu_search():
    """search database for a search_term"""

    while True:
        clear_console()

        print("p. Print db.")
        print("b. Go back.")

        search_term = input("Search: ")

        match search_term:
            case "p":
                input(format_message(DB.dump()))
            case "b":
                break
            case _:
                result = DB.search(search_term)
                if result:
                    input(format_message(result))
                    continue
                input("No matches.")


def update_all() -> int:
    """updates all items in the database"""

    mail_products = list()
    number_updated = 0

    products = DB.dump()

    try:
        # Creates a threadpool with 8 threads.
        with ThreadPoolExecutor(max_workers=12) as executor:
            # Executes the test_update function on every product parallel, saves result to a map in updated_products
            updated_products = executor.map(check_update, products, timeout=20)

        # Commits updated_products to database
        for state, product in updated_products:
            # Right now this will always increment because last_updated will always change.
            if state >= 1:
                number_updated += DB.insert_product_data(product)
                if state == 2:
                    mail_products.append(product)

        # Send mail if list is not empty.
        if mail_products:
            mail_alert(mail_products)

        return number_updated

    except requests.exceptions.ConnectionError:
        print("Site unreachable.")


def check_update(product: Product) -> tuple:
    """check if a product has updated data, returns three states and the product depending on has updated.\n
    0 - Do nothing, nothing has updated.\n
    1 - Insert updated product in db.\n
    2 - Insert AND mail about lower price."""

    try:
        # Creates a new product-object from the supplied products url.
        updated_product = Product(("url", product.url))
    except requests.exceptions.ConnectionError:
        raise

    # If the price of the updated product is the same as the database value. Return False. Mothing has updated.
    if updated_product.price == product.price:
        return (0, product)

    # If the updated price is lower than current, return 2 to mail.
    elif updated_product.price > product.price:
        product.price = updated_product.price
        product.last_updated = updated_product.last_updated

        # If the new price is lower, also set the products lowest_price.
        if product.price < product.lowest_price:
            product.lowest_price = product.price
            product.lowest_price_date = product.last_updated

        return (2, product)

    else:
        return (1, product)


def main():
    menu_items = {
        "1": "Search DB",
        "2": "Add item",
        "3": "Remove item",
        "4": "Update item",
        "5": "Update all",
        "p": "Print DB",
        "e": "Exit",
    }

    while True:
        clear_console()

        for index, (key, item) in enumerate(menu_items.items()):
            print(f"{key}. {item.ljust(12)}", end="")
            if index % 2 == 0:
                print()

        user_choice = input(": ")

        match user_choice:
            case "1":
                menu_search()

            case "2":
                menu_add()

            case "3":
                menu_remove()

            case "4":
                menu_update()

            case "5":
                input(f"{update_all()} product(s) updated.")

            case "p":
                input(format_message(DB.dump()))

            case "e":
                DB.close()
                break

            case _:
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A price-thingy.")
    parser.add_argument("-d", "--daemon", help="update database", action="store_true")
    args = parser.parse_args()

    if args.daemon:
        print("Running update_all every 5 minutes.")
        # Not adding as a background task, it would be tedious to try to kill it if its not user facing.
        # Run as a task or cronjob to update continuously instead.
        while True:
            time.sleep(300)

            # Open db connection. - This is legal?
            DB.__init__(DB.file)

            print(
                f"{time.strftime('%H:%M', time.localtime())} | {update_all()} product(s) updated."
            )

            # Close db so someone can edit it while not updating.
            DB.close()

    else:
        main()
