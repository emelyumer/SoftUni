from project.second_hand_car import SecondHandCar
import unittest


class SecondHandCarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car1 = SecondHandCar("ML350", "SUV", 30_000, 200_000.00)
        self.car2 = SecondHandCar("CLS", "coupe ", 50_000, 150_000.00)
        self.car3 = SecondHandCar("ML500", "SUV", 30_000, 400_000.00)

    def test_all_init(self):
        self.assertEqual("ML350", self.car1.model)
        self.assertEqual("SUV", self.car1.car_type)
        self.assertEqual(30_000, self.car1.mileage)
        self.assertEqual(200_000.00, self.car1.price)
        self.assertEqual([], self.car1.repairs)

    def test_price_setter_raises(self):
        self.assertEqual(200_000.00, self.car1.price)

        with self.assertRaises(ValueError) as ex:
            self.car1.price = 1.0 # 1.0, 0,
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

        self.assertEqual(200_000.00, self.car1.price)

        with self.assertRaises(ValueError) as ex:
            self.car1.price = -0.1
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

        self.assertEqual(200_000.00, self.car1.price)

    def test_price_setter_successful(self):
        self.assertEqual(200_000.00, self.car1.price)

        self.car1.price = 2.0

        self.assertEqual(2.0, self.car1.price)

    def test_mileage_setter_raises(self):
        self.assertEqual(30_000, self.car1.mileage)

        with self.assertRaises(ValueError) as ex:
            self.car1.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

        self.assertEqual(30_000, self.car1.mileage)

        with self.assertRaises(ValueError) as ex:
            self.car1.mileage = -50
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

        self.assertEqual(30_000, self.car1.mileage)

    def test_mileage_setter_successful(self):
        self.assertEqual(30_000, self.car1.mileage)

        self.car1.mileage = 101

        self.assertEqual(101, self.car1.mileage)

        self.car1.mileage = 500

        self.assertEqual(500, self.car1.mileage)

    def test_set_promotional_price_raises(self):
        self.assertEqual(200_000.00, self.car1.price)

        with self.assertRaises(ValueError) as ex:
            self.car1.set_promotional_price(200_000.01)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

        self.assertEqual(200_000.00, self.car1.price)

        with self.assertRaises(ValueError) as ex:
            self.car1.set_promotional_price(200_000.00)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

        self.assertEqual(200_000.00, self.car1.price)

    def test_set_promotional_price_raises_but_setter(self):
        self.assertEqual(200_000.00, self.car1.price)

        with self.assertRaises(ValueError) as ex:
            self.car1.set_promotional_price(-200_000.01)
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

        self.assertEqual(200_000.00, self.car1.price)

    def test_set_promotional_price_successful(self):
        self.assertEqual(200_000.00, self.car1.price)

        self.car1.set_promotional_price(199_999.00)

        self.assertEqual(199_999.00, self.car1.price)

        self.car1.set_promotional_price(150_999.00)

        self.assertEqual(150_999.00, self.car1.price)

    def test_need_repair_impossible(self):
        self.assertEqual(200_000.00, self.car1.price)

        result = self.car1.need_repair(101_001, "engine_repair")

        self.assertEqual('Repair is impossible!', result)
        self.assertEqual(200_000.00, self.car1.price)

    def test_need_repair_test(self):
        self.assertEqual(200_000.00, self.car1.price)

        result = self.car1.need_repair(-100_000, "engine_repair")

        self.assertEqual(100_000.00, self.car1.price)
        self.assertIn("engine_repair", self.car1.repairs)
        self.assertEqual(["engine_repair"], self.car1.repairs)

    def test_need_repair_successful(self):
        self.assertEqual(200_000.00, self.car1.price)

        result = self.car1.need_repair(100_000, "engine_repair")
        self.assertEqual(300_000.00, self.car1.price)
        self.assertIn("engine_repair", self.car1.repairs)
        self.assertEqual(["engine_repair"], self.car1.repairs)

        self.assertEqual(f'Price has been increased due to repair charges.', result)

    def test__gt__type_mismatch(self):
        self.assertEqual("SUV", self.car1.car_type)
        self.assertEqual("coupe ", self.car2.car_type)

        result = self.car1.__gt__(self.car2)

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

        result = self.car2.__gt__(self.car1)

        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test__gt__type_successful(self):
        self.assertEqual("SUV", self.car1.car_type)
        self.assertEqual("SUV", self.car3.car_type)

        result = self.car1.__gt__(self.car3)

        self.assertEqual(False, result)
        self.assertFalse(result)

        result = self.car3.__gt__(self.car1)

        self.assertEqual(True, result)
        self.assertTrue(result)

    def test__str__(self):
        self.assertEqual("ML350", self.car1.model)
        self.assertEqual("SUV", self.car1.car_type)
        self.assertEqual(30_000, self.car1.mileage)
        self.assertEqual(200_000.00, self.car1.price)
        self.assertEqual([], self.car1.repairs)

        result1 = self.car1.__str__()

        self.assertEqual("Model ML350 | Type SUV | Milage 30000km\nCurrent price: 200000.00 | Number of Repairs: 0", result1)

        self.car1.need_repair(50_000, "engine_repair")
        self.assertEqual(250_000.00, self.car1.price)
        self.assertIn("engine_repair", self.car1.repairs)
        self.assertEqual(["engine_repair"], self.car1.repairs)

        result1 = self.car1.__str__()

        self.assertEqual("Model ML350 | Type SUV | Milage 30000km\nCurrent price: 250000.00 | Number of Repairs: 1",
                         result1)

        self.car1.need_repair(50_000, "other")
        self.assertEqual(300_000.00, self.car1.price)
        self.assertIn("other", self.car1.repairs)
        self.assertEqual(["engine_repair", "other"], self.car1.repairs)

        result1 = self.car1.__str__()

        self.assertEqual("Model ML350 | Type SUV | Milage 30000km\nCurrent price: 300000.00 | Number of Repairs: 2",
                         result1)


if __name__ == "__main__":
        unittest.main()











