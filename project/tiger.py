from project.animal import Animal


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int, money_for_care: int):
        super().__init__(self, name: str, gender: str, age: int, money_for_care = 45)