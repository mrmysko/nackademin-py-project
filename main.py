import os

from ExtractData import ExtractData
from DBModule import Database

# Dont make a static db. Allow to change?
db = Database("price.db")


def clear_console():
    """Clears the console on both windows and unix systems."""
    command = "clear"
    if os.name == "nt":
        command = "cls"
    os.system(command)

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")


def print_db(db_items: list):
    """Prints the content of a database formatted."""

    if not db_items:
        print("No match.")
        return

    # Get longest db-name for rjust length.
    longest_name = 0
    for id_, name, price_, url_, last_updated_ in db_items:
        if len(name) > longest_name:
            longest_name = len(name)

    print(
        f'{"ID".ljust(2)} | {"NAME".center(longest_name)} | {"PRICE".center(8)} | {"URL".rjust(0)}'
    )

    # Prints db right-justified by longest product name.
    for id, name, price, url, last_updated_ in db_items:
        print(
            f"{str(id).rjust(2)} | {name.rjust(longest_name)} | {format_price(price).rjust(8)} | {url.rjust(0)}"
        )


def remove_menu():
    """User-facing menu for removing items from database."""

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
                        print(f"{product.name} removed.")
                        input()
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


def update_menu():
    """User-facing menu for updating database items."""

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

            if db.update_product_data(product):
                print(f"{product.name} updated.")
                input()
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


def add_menu():
    """User-facing menu for adding items to database."""

    clear_console()

    url = input("URL: ")
    product = ExtractData(url)

    if db.insert_product_data(product):
        print(f"Added {product.name} to database.")
        input()


def search_menu():
    while True:
        clear_console()

        print("b. Go back.")

        search_term = input("Search: ")

        match search_term:

            case "b":
                break

            case _:
                pass

        result = db.search_db(search_term)

        print_db(result)
        input()


def format_price(price: int) -> str:
    """formats price to a human readable form."""

    price = f"{int(price):,} :-".replace(",", " ")

    return price


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

        for key, item in menu_items.items():
            print(f"{key}. {item}.")

        user_choice = input(": ")

        match user_choice:
            case "1":
                search_menu()

            case "2":
                add_menu()

            case "3":
                remove_menu()

            case "4":
                update_menu()

            case "5":
                rows_updated = db.update_all()
                print(f"{rows_updated} product(s) updated.")
                input()

            case "p":
                print_db(db.dump_db())
                input()

            case "e":
                db.close_db()
                break

            case _:
                pass


if __name__ == "__main__":
    main()
