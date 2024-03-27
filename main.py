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


# This dialog-tree is ugly.
while True:
    clear_console()

    print("|--------------|")
    print("| Price-thingy | - Netonnet edition")
    print("|--------------|")
    print("1. Query item.")
    print("2. Add item.")
    print("3. Remove item.")
    print("p. Print DB.")
    print("e. Exit")

    # Locals returns a list of local variables and symbols(?) in the current program.
    if "product" in locals():
        print(f"Stored Query: {product.name} {product.price}")
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
        while True:
            clear_console()

            print("Which item would you like to remove? (id)")
            print("p. Print DB.")
            print("b. Go back.")
            user_choice = input(": ")
            match user_choice:
                case int():
                    db.remove_product_data(user_choice)
                case "p":
                    db.print_db()
                    input()
                case "b":
                    break
                case _:
                    pass
        db.remove_product_data(user_choice)

    elif user_choice.lower() == "p":
        db.print_db()
        input()

    elif user_choice.lower() == "e":
        break
