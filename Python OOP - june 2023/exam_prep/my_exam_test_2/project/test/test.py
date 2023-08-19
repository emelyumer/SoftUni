from project.trip import Trip
import unittest


class TripTest(unittest.TestCase):
    def setUp(self) -> None:
        self.trip1 = Trip(2000.0, 2, True)
        self.trip2 = Trip(1500.0, 1, False)
        self.trip3 = Trip(50000.0, 5, False)
        self.trip4 = Trip(80000.0, 4, True)

    def test_correct_init(self):
        self.assertEqual(2000.0, self.trip1.budget)
        self.assertEqual(2, self.trip1.travelers)
        self.assertEqual(True, self.trip1.is_family)
        self.assertEqual(False, self.trip2.is_family)
        self.assertEqual({}, self.trip1.booked_destinations_paid_amounts)
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, Trip.DESTINATION_PRICES_PER_PERSON)

    def test_setter_travelers_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.trip1.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.trip1.travelers = -1
        self.assertEqual('At least one traveler is required!', str(ex.exception))

    def test_setter_travelers_successful(self):
        self.assertEqual(2, self.trip1.travelers)
        self.trip1.travelers = 1
        self.assertEqual(1, self.trip1.travelers)
        self.trip1.travelers = 2
        self.assertEqual(2, self.trip1.travelers)
        self.trip1.travelers = 10
        self.assertEqual(10, self.trip1.travelers)

    def test_setter_is_family(self):
        self.assertEqual(True, self.trip1.is_family)
        self.trip1.is_family = False
        self.assertEqual(False, self.trip1.is_family)

        self.assertEqual(False, self.trip2.is_family)
        self.trip2.is_family = True
        self.assertEqual(False, self.trip2.is_family)

        self.assertEqual(False, self.trip3.is_family)
        self.trip3.is_family = True
        self.assertEqual(True, self.trip3.is_family)

    def test_book_a_trip(self):
        self.trip2.book_a_trip("USA")
        self.assertEqual('This destination is not in our offers, please choose a new one!', self.trip2.book_a_trip("USA"))

        self.trip2.book_a_trip("New Zealand")
        self.assertEqual('Your budget is not enough!', self.trip2.book_a_trip("New Zealand"))

        self.trip2.book_a_trip("Bulgaria")
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 500.00", self.trip2.book_a_trip("Bulgaria"))

    def test_booking_status(self):
        self.trip1.booking_status()
        self.assertEqual("No bookings yet. Budget: 2000.00", self.trip1.booking_status())

        self.trip2.book_a_trip("Bulgaria")
        self.assertEqual("Successfully booked destination Bulgaria! Your budget left is 500.00",
                         self.trip2.book_a_trip("Bulgaria"))
        self.trip2.booking_status()
        self.assertEqual("Booked Destination: Bulgaria\nPaid Amount: 500.00\nNumber of Travelers: 1\nBudget Left: 500.00", self.trip2.booking_status())

    def test_general(self):
        self.trip4.book_a_trip("New Zealand")
        self.assertEqual("Successfully booked destination New Zealand! Your budget left is 26000.00",
                        self.trip4.book_a_trip("New Zealand"))
        self.assertEqual({'New Zealand': 27000.0}, self.trip4.booked_destinations_paid_amounts)

        self.trip4.book_a_trip("'Brazil': 6200")
        self.assertEqual("Successfully booked destination Brazil! Your budget left is 3680.00",
                         self.trip4.book_a_trip("Brazil"))
        self.assertEqual({'Brazil': 22320.0, 'New Zealand': 27000.0}, self.trip4.booked_destinations_paid_amounts)