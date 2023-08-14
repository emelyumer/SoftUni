from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.truck_driver1 = TruckDriver("Petar", 1.00)

    def test_correct_init(self):
        self.assertEqual("Petar", self.truck_driver1.name)
        self.assertEqual(1.00, self.truck_driver1.money_per_mile)
        self.assertEqual({}, self.truck_driver1.available_cargos)
        self.assertEqual(0, self.truck_driver1.earned_money)
        self.assertEqual(0, self.truck_driver1.miles)

    def test_setter_earned_money_raises(self):
        self.assertEqual(0, self.truck_driver1.earned_money)

        with self.assertRaises(ValueError) as ex:
            self.truck_driver1.earned_money = -1

        self.assertEqual("Petar went bankrupt.", str(ex.exception))

    def test_setter_earned_money_successful(self):
        self.assertEqual(0, self.truck_driver1.earned_money)
        self.truck_driver1.earned_money = 1
        self.assertEqual(1, self.truck_driver1.earned_money)

    def test_add_cargo_offer_raises(self):
        self.truck_driver1.available_cargos["Sofia"] = 100
        result = self.truck_driver1.available_cargos
        self.assertEqual({"Sofia": 100}, result)

        with self.assertRaises(Exception) as ex:
            self.truck_driver1.add_cargo_offer("Sofia", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_successful(self):
        self.truck_driver1.available_cargos["Sofia"] = 100
        result = self.truck_driver1.available_cargos
        self.assertEqual({"Sofia": 100}, result)

        result = self.truck_driver1.add_cargo_offer("Montana", 50)
        self.assertEqual("Cargo for 50 to Montana was added as an offer.", result)
        self.assertEqual({"Montana": 50, "Sofia": 100}, self.truck_driver1.available_cargos)

    def test_drive_best_cargo_offer_raises(self):
        self.assertEqual({}, self.truck_driver1.available_cargos)

        result = self.truck_driver1.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_successful(self):
        self.truck_driver1.add_cargo_offer("Sofia", 100)
        self.truck_driver1.add_cargo_offer("Montana", 80)

        result = self.truck_driver1.drive_best_cargo_offer()

        self.assertEqual("Petar is driving 100 to Sofia.", result)
        self.assertEqual(100, self.truck_driver1.earned_money)
        self.assertEqual(100, self.truck_driver1.miles)
        self.assertEqual(None, self.truck_driver1.check_for_activities(100))

    # def test_check_for_activities(self):

    def test_eat_active_passive(self):
        self.truck_driver1.earned_money = 1000
        self.assertEqual(1000, self.truck_driver1.earned_money)

        self.truck_driver1.eat(100)
        self.assertEqual(1000, self.truck_driver1.earned_money)

        self.truck_driver1.eat(250)
        self.assertEqual(980, self.truck_driver1.earned_money)

        self.truck_driver1.eat(500)
        self.assertEqual(960, self.truck_driver1.earned_money)

        self.truck_driver1.eat(600)
        self.assertEqual(960, self.truck_driver1.earned_money)

    def test_sleep_active_passive(self):
        self.truck_driver1.earned_money = 1000
        self.assertEqual(1000, self.truck_driver1.earned_money)

        self.truck_driver1.sleep(250)
        self.assertEqual(1000, self.truck_driver1.earned_money)

        self.truck_driver1.sleep(1000)
        self.assertEqual(955, self.truck_driver1.earned_money)

    def test_pump_gas_active_passive(self):
        self.truck_driver1.earned_money = 1000
        self.assertEqual(1000, self.truck_driver1.earned_money)

        self.truck_driver1.pump_gas(250)
        self.assertEqual(1000, self.truck_driver1.earned_money)

        self.truck_driver1.pump_gas(1500)
        self.assertEqual(500, self.truck_driver1.earned_money)

    def test_repair_truck_active_passive(self):
        self.truck_driver1.earned_money = 10000
        self.assertEqual(10000, self.truck_driver1.earned_money)

        self.truck_driver1.repair_truck(9999)
        self.assertEqual(10000, self.truck_driver1.earned_money)

        self.truck_driver1.repair_truck(10000)
        self.assertEqual(2500, self.truck_driver1.earned_money)

    def test_repr(self):
        self.truck_driver1.miles = 5401
        self.assertEqual(5401, self.truck_driver1.miles)

        self.truck_driver1.__repr__()
        self.assertEqual("Petar has 5401 miles behind his back.", self.truck_driver1.__repr__())

    def test_general(self):
        self.truck_driver1.add_cargo_offer("Varna", 80)
        self.truck_driver1.add_cargo_offer("Sofia", 2000)
        self.truck_driver1.add_cargo_offer("Ruse", 60)

        self.assertEqual({"Ruse": 60, "Sofia": 2000, "Varna": 80}, self.truck_driver1.available_cargos)

        with self.assertRaises(Exception) as ex:
            self.truck_driver1.add_cargo_offer("Ruse", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

        result = self.truck_driver1.drive_best_cargo_offer()
        self.assertEqual("Petar is driving 2000 to Sofia.", result)
        self.assertEqual(1250.0, self.truck_driver1.earned_money)
        self.assertEqual(2000, self.truck_driver1.miles)

        self.truck_driver1.add_cargo_offer("New York", 3000)
        result = self.truck_driver1.drive_best_cargo_offer()
        self.assertEqual("Petar is driving 3000 to New York.", result)
        self.assertEqual(2875.0, self.truck_driver1.earned_money)
        self.assertEqual(5000, self.truck_driver1.miles)


if __name__ == "__main__":
    unittest.main()

