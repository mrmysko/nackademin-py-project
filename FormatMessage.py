import os


def format_message(products: list):
    """prints the content of a database formatted."""

    if not products:
        print("Database empty.")
        return

    message = []

    # Get longest db-name for rjust length. Also cap name printout to 40 chars.
    longest_name = 0
    for product in products:
        if len(product.name) > 40:
            longest_name = 40
            break
        elif len(product.name) > longest_name:
            longest_name = len(product.name)

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


# Alternative formatting
# for product in products:
#    print(
#        f"""| {str(product.id).rjust(2)}. {product.name}
# | Current Price: {format_price(product.price).rjust(10)}
# |  Lowest Price: {format_price(product.lowest_price).rjust(10)}
# | {product.url.rjust(0)}
# |"""
#        )


def format_price(price: int) -> str:
    """formats price to a human readable form."""

    price = f"{int(price):,} :-".replace(",", " ")

    return price
