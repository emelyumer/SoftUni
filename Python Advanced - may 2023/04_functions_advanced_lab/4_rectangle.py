def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    def area():
        return length * width


    def parameter():
        return 2 * length + 2 * width

    return f"Rectangle area: {area()}\nRectangle perimeter: {parameter()}"

print(rectangle("2", 10))