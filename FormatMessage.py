import os


def format_message(products: list, alt_format=False) -> str:
    """returns the content of a list of products as a formatted string."""

    if not products:
        print("Database empty.")
        return

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
    """formats price to a prettier form."""

    price = f"{int(price):,} :-".replace(",", " ")

    return price
