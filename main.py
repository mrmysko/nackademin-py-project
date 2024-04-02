import os
import argparse
import time

from pathlib import Path
from Product import Product
from Database import Database
from concurrent.futures import ThreadPoolExecutor
from FormatMessage import format_message
from MailAlert import mail_alert


def clear_console():
    """clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")

    line = f'{"Hej" if True else ""}'
    print(line)

    print(os.get_terminal_size()[0])  # Use to dynamically adjust name-length.


def remove_menu(db: Database):
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

            product = db.get_product_data(user_choice)

            print(f"Confirm removal of: {product.name}")
            print("(y/n)")

            user_confirm = input(": ")
            match user_confirm.lower():
                case "y":
                    if db.remove_product_data(product):
                        input(f"{product.name} removed.")
                case _:
                    pass

        except ValueError:
            match user_choice:
                case "p":
                    print(format_message(db.dump_db()))
                    input()
                case "b":
                    break
                case _:
                    pass


def update_menu(db: Database):
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

            product = db.get_product_data(user_choice)

            status, product = check_update(product)

            # Status 2 in a manual update doesnt require a mail.
            if status == 1 or status == 2:
                if db.insert_product_data(product):
                    input(f"{product.name} updated.")
                    continue
                else:
                    input("Could not update database.")
                    continue
            print(f"{product.name} already up to date.")
            input()

        except ValueError:
            match user_choice:
                case "p":
                    print(format_message(db.dump_db()))
                    input()
                case "b":
                    break
                case _:
                    pass


def add_menu(db: Database):
    """user-facing menu for adding items to database."""

    clear_console()

    url = input("URL: ")
    product = Product(("url", url))

    # Check if product is in database, else add it.
    if not db.insert_product_data(product):
        input(f"Could not add {product.name} to database.")
    else:
        input(f"Added {product.name} to database.")


def search_menu(db: Database):
    """search database for a search_term"""

    while True:
        clear_console()

        print("p. Print db.")
        print("b. Go back.")

        search_term = input("Search: ")

        match search_term:
            case "p":
                print(format_message(db.dump_db()))
                input()
            case "b":
                break
            case _:
                result = db.search_db(search_term)
                if result:
                    print(format_message(result))
                    input()
                    continue
                input("No matches.")


def update_all() -> int:
    """updates all items in the database"""

    mail_products = list()
    products_updated = 0

    products = db.dump_db()

    # Creates a threadpool with 8 threads.
    with ThreadPoolExecutor(max_workers=8) as executor:
        # Executes the test_update function on every product parallel, saves result to a map in updated_products
        updated_products = executor.map(check_update, products)

    # Commits updated_products to database
    for state, product in updated_products:
        # Right now this will always increment because last_updated will always change.
        if state >= 1:
            products_updated += db.insert_product_data(product)
            if state == 2:
                mail_products.append(product)

    # Send mail if list is not empty.
    if mail_products:
        mail_alert(mail_products)

    return products_updated


def check_update(product: Product) -> tuple:
    """check if a product has updated data, returns three states and the product depending on has updated.\n
    0 - Do nothing, nothing has updated.\n
    1 - Insert updated product in db.\n
    2 - Insert AND mail about lower price."""

    # Creates a new product-object from the supplied products url.
    updated_product = Product(("url", product.url))

    # If the price of the updated product is the same as the database value. Return False. Mothing has updated.
    if updated_product.price == product.price:
        return (0, product)

    # Else set the price of the product to the price of the updated product.
    else:
        product.price = updated_product.price
        product.last_updated = updated_product.last_updated

        # If the new price is lower, also set the products lowest_price.
        if product.price < product.lowest_price:
            product.lowest_price = product.price
            product.lowest_price_date = product.last_updated
            return (2, product)

        return (1, product)


def main(db: Database):
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

        for key, item in menu_items.items():
            print(f"{key}. {item}.")

        user_choice = input(": ")

        match user_choice:
            case "1":
                search_menu(db)

            case "2":
                add_menu(db)

            case "3":
                remove_menu(db)

            case "4":
                update_menu(db)

            case "5":
                input(f"{update_all()} product(s) updated.")

            case "p":
                print(format_message(db.dump_db()))
                input()

            case "e":
                db.close_db()
                break

            case _:
                pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A price-thingy.")
    parser.add_argument("-d", "--daemon", help="update database", action="store_true")
    args = parser.parse_args()

    # Dont make a static db. Allow to change?
    # Opens price.db placed in programs root folder.
    db_path = Path(__file__).with_name("price.db")

    db = Database(db_path)

    if args.daemon:
        print("Running update_all every 3 minutes.")
        # Not adding as a background task, it would be tedious to try to kill it if its not user facing.
        # Run as a task or cronjob to update continuously instead.
        while True:
            time.sleep(180)

            # Open db connection. - This is legal?
            db.__init__(db.file)

            print(
                f"{time.strftime('%H:%M', time.localtime())} | {update_all()} product(s) updated."
            )

            # Close db so someone can edit it while not updating.
            db.close_db()

    else:
        main(db)
