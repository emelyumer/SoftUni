from typing import List

from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def food_that_eats(self) -> List:
        return [Vegetable, Fruit]

    def gained_weight(self) -> float:
        return 0.10


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def food_that_eats(self) -> List:
        return [Meat]

    def gained_weight(self) -> float:
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def food_that_eats(self) -> List:
        return [Vegetable, Meat]

    def gained_weight(self) -> float:
        return 0.30


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def food_that_eats(self) -> List:
        return [Meat]

    def gained_weight(self) -> float:
        return 1.00
