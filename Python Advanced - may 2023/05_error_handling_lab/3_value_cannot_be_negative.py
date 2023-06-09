class ValueCannotBeNegative():
    pass


for _ in range(5):
    try:
        number = float(input("Enter a number"))
        if number < 0:
            raise ValueCannotBeNegative
    except ValueError:
        print("This not valid number, continue to the next one")


