import pytest


fn_name = "stringt"


class ImportDetailsError(Exception):
    pass


try:
    import uppgift

    fn = getattr(uppgift, fn_name)

    if not callable(fn):
        raise ImportDetailsError(f"Function {fn_name} is not callable")

    # Alt #1:
    #
    if not fn.__code__.co_argcount == 2:
        raise ImportDetailsError(f"Function {fn_name} must take exactly two arguments")

    # Alt #2:
    #
    # Kontrollera att funktionen accepterar en variabel mängd argument
    # Notera: Vi kan inte enkelt kontrollera antalet positionella argument för
    # en funktion som accepterar *args, så vi hoppar över den kontrollen här.

    def test_exempel_1():
        assert fn("Hej", "världen", sep=", ", end="!") == "Hej, världen!"

    def test_exempel_2():
        assert fn("Python", "är", "kul") == "Python är kul\n"

    def test_exempel_3():
        assert fn("En", "två", "tre", sep=" - ") == "En - två - tre\n"

    def test_exempel_4():
        assert fn("Slut", end=".") == "Slut."

    def test_exempel_5():
        assert fn("Ett", "argument", sep="") == "Ettargument\n"

    def test_exempel_6():
        assert fn("Ensam") == "Ensam\n"

except ImportDetailsError as e:
    pytest.fail(str(e))

except ImportError:
    pytest.fail(f"Function {fn_name} has not been implemented")
