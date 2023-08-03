import unittest
from project.vehicle import Vehicle

class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.00, 200.00)

    def test_all_init(self):
        self.assertEqual(10.00, self.vehicle.fuel)
        self.assertEqual(10.00, self.vehicle.capacity)
        self.assertEqual(200.00, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_raises(self):
        self.assertEqual(10.00, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

        self.assertEqual(10.00, self.vehicle.fuel)

    def test_drive_successful(self):
        self.assertEqual(10.00, self.vehicle.fuel)

        self.vehicle.drive(4)

        self.assertEqual(5.00, self.vehicle.fuel)

    def test_refuel_raises(self):
        self.assertEqual(10.00, self.vehicle.fuel)
        self.assertEqual(10.00, self.vehicle.capacity)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

        self.assertEqual(10.00, self.vehicle.fuel)
        self.assertEqual(10.00, self.vehicle.capacity)

    def test_refuel_successful(self):
        self.vehicle.fuel = -1
        self.vehicle.refuel(1)

        self.assertEqual(0, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual(
            "The vehicle has 200.0 horse power with 10.0 fuel left and 1.25 fuel consumption", self.vehicle.__str__()
        )


if __name__ == "__main__":
    unittest.main()