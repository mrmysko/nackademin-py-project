###############################################
# REPO MOVED TO mrmysko/nackademin-py-project #
###############################################

import argparse
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from Database import Database
from helper import check_update, clear_console, format_message, get_url_data
from mail_alert import mail_alert
from Product import Product


def menu_print(menu_items={"p": "Print DB.", "b": "Go back."}):
    """
    Prints the menu.
    """

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")

    for index, (key, item) in enumerate(menu_items.items()):
        print(f"{key}. {item.ljust(12)}", end="")
        if index % 2 == 0:
            print()


def menu_search():
    """
    Prompts for a search term and search DB for it.
    """

    while True:
        clear_console()
        menu_print()

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
                input("No matches found.")


def menu_add():
    """
    Prompts for URL and add it's product to DB.
    """

    while True:
        clear_console()
        menu_print()

        url = input("URL: ")

        match url:
            case "p":
                input(format_message(DB.dump()))
            case "b":
                break
            case _:
                try:
                    product = Product(*get_url_data(url))

                    # Check if product is in database, else add it.
                    if not DB.insert_product_data(product):
                        message = f"Could not add '{product.name}' to database."
                    else:
                        message = f"Added '{product.name}' to database."

                except AttributeError:
                    message = "Data not found in URL."
                # Do I really need to import requests just to catch a raised error?
                except requests.exceptions.RequestException:
                    message = f"Unreachable: {url}"

                input(message)


def menu_remove():
    """
    Prompts for ID and removes it from DB.
    """

    while True:
        clear_console()
        menu_print()

        user_choice = input("ID: ")

        if user_choice.isdigit():
            product = DB.get_product_data(user_choice)

            if not product:
                input("Index not found.")
                continue

            print(f"Confirm removal of '{product.name}'")
            print("y / (n)")

            user_choice = input(": ")
            match user_choice.lower():
                case "y":
                    if DB.remove_product_data(product):
                        input(f"'{product.name}' removed.")
                case _:
                    pass

        else:
            match user_choice:
                case "p":
                    input(format_message(DB.dump()))
                case "b":
                    break
                case _:
                    pass


def menu_update():
    """
    Prompts for ID and updates it in DB.
    """

    while True:
        clear_console()
        menu_print()

        user_choice = input("ID: ")

        # Hey, thats illegal.
        if user_choice.isdigit():
            product = DB.get_product_data(user_choice)

            if not product:
                input("Index not found.")
                continue

            try:
                status, product = check_update(product)
            except requests.exceptions.RequestException:
                input(f"Unreachable: {product.url}")
                continue
            except AttributeError:
                input(f"Data of '{product.name}' not found in URL.")
                continue

            if status:
                if DB.insert_product_data(product):
                    input(f"'{product.name}' updated.")
                    continue
                # It's impossible to get here afaik.
                else:
                    input("Could not update database.")
                    continue
            input(f"'{product.name}' already up to date.")

        else:
            match user_choice:
                case "p":
                    input(format_message(DB.dump()))
                case "b":
                    break
                case _:
                    pass


def update_all() -> int:
    """
    Updates all items in the database.
    """

    mail_products = list()
    updated_products = list()
    number_updated = 0

    products = DB.dump()

    def handle_check_update_error(product: Product):
        """handles errors in called funvtions so the entire threadpool doesnt fail."""

        try:
            return check_update(product)
        except requests.exceptions.RequestException:
            print(f"Unreachable: {product.url}")
            return (0, product)
        except AttributeError:
            print(f"Data of '{product.name}' not found in URL.")
            return (0, product)

    # Creates a threadpool with 8 threads.
    with ThreadPoolExecutor(max_workers=12) as executor:
        # Executes the test_update function on every product parallel, saves result to a map in checked_products
        checked_products = executor.map(handle_check_update_error, products, timeout=20)

    # Commits checked_products to database
    for state, product in checked_products:
        # Right now this will always increment because last_updated will always change.
        if state >= 1:
            updated_products.append(product)
            number_updated += DB.insert_product_data(product)
            if state == 2:
                mail_products.append(product)

    print(format_message(updated_products))

    # Send mail if list is not empty.
    if mail_products:
        print(mail_alert(mail_products))

    return number_updated


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
        menu_print(menu_items)

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
    parser.add_argument("-f", "--file", help="specify file")
    args = parser.parse_args()

    # Opens price.db placed in programs root folder.
    if args.file:
        DB_PATH = Path(__file__).with_name(args.file)
    else:
        DB_PATH = Path(__file__).with_name("price.sql")

    DB = Database(DB_PATH)

    if args.daemon:
        print("Running update_all every 5 minutes.")
        # Not adding as a background task, it would be tedious to try to kill it if its not user facing.
        # Run as a task or cronjob to update continuously instead.

        try:
            while True:
                time.sleep(300)

                print(
                    f"{time.strftime('%H:%M', time.localtime())} | {update_all()} product(s) updated."
                )

        except KeyboardInterrupt:
            print("Exiting...")
            DB.close()

    else:
        main()
