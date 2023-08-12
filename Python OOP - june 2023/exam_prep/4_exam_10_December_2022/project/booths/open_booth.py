from project.booths.booth import Booth


class OpenBooth(Booth):
    RESERVATION_PRICE = 2.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = OpenBooth.RESERVATION_PRICE * number_of_people
        self.is_reserved = True
