from project.booths.booth import Booth


class PrivateBooth(Booth):
    RESERVATION_PRICE = 3.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = PrivateBooth.RESERVATION_PRICE * number_of_people
        self.is_reserved = True
