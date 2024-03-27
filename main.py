# Notes:
# Selenium verkar onödigt stort, en hel webbläsarmotor för en request.
# Webhallen anävnder ett js för att generera typ hela deras webbsida, pivot till netonnet KEKL

"""Behöver produkter ens ha en klass? Vad ska jag göra med ett klassobjekt som är en produkt? 
Just nu har den inga metoder, men om den skulle ha det, vad skulle det vara? 
Och hur accesar jag det objektet om jag inte queryat med en länk?"""

""""Adaptor-funktionen", så iman har man en funktion som...hämtar data och standardiserar den? 
Den skulle då kalla på en metod från en...en butik för att få datan? 
Var går skiljelinjen vad som ska hanteras av klassen och vad som kommer från "adaptorn" då? """

# bs4
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# sqlite3
# https://docs.python.org/3/library/sqlite3.html

# Todo - Gör klart uppdatera och ta bort databas-grejer.
# Todo - Få ut mer data/kategorier från items? https://www.netonnet.se/art/dator-surfplatta/laptop/laptop-14-16-tum/angstrom-angstrom-m1home/1028915.8908/ t.ex. Kommer ut som "Ångström  (M1HOME)", vilket inte säger någonting. (Det är en laptop btw.)
# Todo - Stäng databasen.
# Todo - Options (verbose?) och mer output när saker händer till konsolen.
# Todo - Felhantering: Fel länk, hittar inte element, databasen går inte att öppna, hittar inte någor i databasen, om användaren skriver in fel.
# Todo - Type-hinta och kommentera
# Todo - Evaluate meningen med att ha en klass för produkter, vad ville jag ens göra med den? Eller koppla ihop databasen med produkter by id elr nått. Så man kan göra lookups på databasen och få ut ett produktobjekt.

import os

from ExtractData import ExtractData
from DBModule import Database
from Product import Product

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


def print_db():

    # Get longest db-name for rjust length.
    longest_name = 0
    for id_, name, price_, url_ in db.dump_db():
        if len(name) > longest_name:
            longest_name = len(name)

    print(
        f'{"ID".rjust(2)} {"NAME".center(longest_name)} {"PRICE".rjust(5)} {"URL".rjust(0)}'
    )

    # Prints db right-justified by longest product name.
    for id, name, price, url in db.dump_db():
        print(
            f"{str(id).rjust(2)} {name.rjust(longest_name)} {price.rjust(5)} {url.rjust(0)}"
        )


def remove_menu():
    while True:
        clear_console()

        print("Which item would you like to remove? (id)")
        print("p. Print DB.")
        print("b. Go back.")
        user_choice = input(": ")

        # How do I check against both str and int input?
        # 1. input
        # 2. Check if that input CAN become an int with try? - "Bad, only use try for exceptional errors" - Kent
        # 3. If it is an int, do the remove thing?
        # 4. Else: do the match case thing?

        # Hey, thats illegal.
        try:
            int(user_choice)
            # If im using classes for products, this should just be product.name tbh. So ask for product -> Fetch the product to a class object -> dosplay name.
            print(f"Confirm removal of: {db.get_product_data(user_choice)[1]}")
            print("(y/n)")
            user_confirm = input(": ")
            match user_confirm.lower():
                case "y":
                    print(f"{db.remove_product_data(user_choice)} row(s) removed.")
                    input()
                case _:
                    pass

        except ValueError:
            match user_choice:
                case "p":
                    print_db()
                    input()
                case "b":
                    break
                case _:
                    pass


def update_menu():
    while True:
        clear_console()

        print("Which item would you like to update? (id)")
        print("p. Print DB.")
        print("b. Go back.")
        user_choice = input(": ")

        # Hey, thats illegal.
        try:
            int(user_choice)
            print(f"{db.update_product_data(user_choice)} row(s) updated.")
            input()

        except ValueError:
            match user_choice:
                case "p":
                    print_db()
                    input()
                case "b":
                    break
                case _:
                    pass


# This dialog-tree is ugly.
while True:
    clear_console()

    print("1. Query item.")
    print("2. Add item.")
    print("3. Remove item.")
    print("4. Update item.")
    print("p. Print DB.")
    print("e. Exit")

    # Locals returns a list of local variables and symbols(?) in the current program.
    if "product" in locals():
        print(f"Stored Query: {product.name} {product.price}")
    # print("3. Query DB.")

    user_choice = input(": ")

    if user_choice == "1":

        url = input("URL: ")
        name, price, url = ExtractData(url)

        product = Product(name, price, url)

        print(name)
        print(price)
        input()

    elif user_choice == "2":
        db.insert_product_data((product.name, product.price, product.url))

    elif user_choice == "3":
        remove_menu()

    elif user_choice == "4":
        update_menu()

    elif user_choice.lower() == "p":
        print_db()
        input()

    elif user_choice.lower() == "e":
        break
