from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPE = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPE = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = [d for d in self.delicacies if d.name == name]

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY_TYPE:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = ChristmasPastryShopApp.VALID_DELICACY_TYPE[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = [b for b in self.booths if b.booth_number == booth_number]

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH_TYPE:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = ChristmasPastryShopApp.VALID_BOOTH_TYPE[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        delicacy = [d for d in self.delicacies if d.name == delicacy_name]
        booth = [b for b in self.booths if b.booth_number == booth_number]

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth[0].delicacy_orders.append(delicacy[0])
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        price = booth.price_for_reservation + sum([o.price for o in booth.delicacy_orders])
        self.income += price
        booth.is_reserved = False
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0.0
        return f"Booth {booth_number}:\n" \
               f"Bill: {price:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
