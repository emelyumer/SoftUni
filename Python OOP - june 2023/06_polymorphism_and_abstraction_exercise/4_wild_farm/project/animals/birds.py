from typing import List

from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    # @property
    def make_sound(self):
        return "Hoot Hoot"

    # @property
    def food_that_eats(self) -> List:
        return [Meat]

    # @property
    def gained_weight(self) -> float:
        return 0.25


class Hen(Bird):
    # @property
    def make_sound(self):
        return "Cluck"

    # @property
    def food_that_eats(self) -> List:
        return [Vegetable, Fruit, Meat, Seed]

    # @property
    def gained_weight(self) -> float:
        return 0.35



