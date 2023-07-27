from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.username)


class Group:
    def __init__(self, name: str, people):
        self.name = name
        self.people: List[Person] = []

    def __add__(self, other):

        return Group(f"{self.name} {other.name}", sum(len(self.people) + len(other.people)))
