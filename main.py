import os
import sys
import argparse
import time

from Product import Product
from DBModule import Database
from concurrent.futures import ThreadPoolExecutor


def clear_console():
    """clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")


def print_db(products: list):
    """prints the content of a database formatted."""

    if not products:
        print("Database empty.")
        return

    # Get longest db-name for rjust length.
    longest_name = 0
    for product in products:
        if len(product.name) > longest_name:
            longest_name = len(product.name)

    print(
        f'{"ID".ljust(2)} | {"NAME".center(longest_name)} | {"CUR PRICE".center(10)} | {"LOW PRICE".rjust(10)} | {"URL".rjust(0)}'
    )

    # Prints db right-justified by longest product name.
    for product in products:
        print(
            f"{str(product.id).rjust(2)} | {product.name.rjust(longest_name)} | {format_price(product.price).rjust(10)} | {format_price(product.lowest_price).rjust(10)} | {product.url.rjust(0)}"
        )


# Alternative formatting
# for product in products:
#    print(
#        f"""| {str(product.id).rjust(2)}. {product.name}
# | Current Price: {format_price(product.price).rjust(10)}
# |  Lowest Price: {format_price(product.lowest_price).rjust(10)}
# | {product.url.rjust(0)}
# |"""
#        )


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
                    print_db(db.dump_db())
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

            if product.update():
                if db.update_product_data(product):
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
                    print_db(db.dump_db())
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

    if db.insert_product_data(product):
        input(f"Added {product.name} to database.")
    else:
        input("Could not add to database.")


def search_menu(db: Database):
    """search database for a search_term"""

    while True:
        clear_console()

        print("p. Print db.")
        print("b. Go back.")

        search_term = input("Search: ")

        match search_term:
            case "p":
                print_db(db.dump_db())
                input()
            case "b":
                break
            case _:
                result = db.search_db(search_term)
                if result:
                    print_db(result)
                    input()
                    continue
                input("No matches.")


def update_all() -> int:
    """updates all items in the database"""

    products_updated = 0

    products = db.dump_db()

    # lambda this?
    def test_update(product):
        return product.update()

    # Creates a threadpool with 8 threads.
    with ThreadPoolExecutor(max_workers=8) as executor:
        # Executes the test_update function on every product parallel, saves result to a map in updated_products
        updated_products = executor.map(test_update, products)

    # Commits updated_products to database
    for product in updated_products:
        # Right now this will always increment because last_updated will always change.
        products_updated += db.update_product_data(product)

    return products_updated


def format_price(price: int) -> str:
    """formats price to a human readable form."""

    price = f"{int(price):,} :-".replace(",", " ")

    return price


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
                print_db(db.dump_db())
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

    if args.daemon:
        print("Running update_all every 3 minutes.")
        # Not adding as a background task, it would be tedious to try to kill it if its not user facing.
        # Run as a task or cronjob to update continuously instead.
        while True:
            time.sleep(180)

            db = Database(sys.path[0] + "\\price.db")

            print(
                f"{time.strftime("%H:%M", time.localtime())} | {update_all()} product(s) updated."
            )

            # Close db so someone can edit it while not updating.
            db.close_db()

    else:
        # Dont make a static db. Allow to change?
        # Opens price.db placed in programs root folder.
        db = Database(sys.path[0] + "\\price.db")

        main(db)
