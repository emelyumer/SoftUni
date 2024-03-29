class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.area = self.get_area()

    def get_area(self):
        return self.width * self.height

    def __gt__(self, other):
        return self.area > other.area

    def __ne__(self, other):
        return self.area != other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ge__(self, other):
        return self.area >= other.area


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)


