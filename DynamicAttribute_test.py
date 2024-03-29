import sqlite3

""" description

    Read-only attribute that provides the column names of the last query. 
    To remain compatible with the Python DB API, it returns a 7-tuple for each 
    column where the last six items of each tuple are None."""


# Dynamic attribute test


class Test:
    def __init__(self):
        pass


def main():

    some_thing = Test()

    connection = sqlite3.connect("price.db")

    cursor = connection.cursor()

    matches = cursor.execute("SELECT * FROM products")

    columns = [col[0] for col in cursor.description]

    print(columns)

    for row in matches:
        for attr, value in zip(columns, row):
            setattr(some_thing, attr, value)

    print(some_thing.id)
    print(some_thing.name)


if __name__ == "__main__":
    main()
