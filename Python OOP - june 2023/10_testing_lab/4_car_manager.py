class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


import unittest

class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "X5", 8.4, 68)
    def test_init_list_all_ints(self):
        test_car = Car("BMW", "X5", 8.4, 68)
        self.assertEqual("BMW", test_car.make)
        self.assertEqual("X5", test_car.model)
        self.assertEqual(8.4, test_car.fuel_consumption)
        self.assertEqual(68, test_car.fuel_capacity)
        self.assertEqual(0, test_car.fuel_amount)

    def test_make_setter_raise(self):
        self.assertEqual("BMW", self.car.make)

        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        self.assertEqual("BMW", self.car.make)

    def test_make_setter_successfully_changed(self):
        self.assertEqual("BMW", self.car.make)

        self.car.make = "Audi"
        self.assertEqual("Audi", self.car.make)

    def test_model_setter_raise(self):
        self.assertEqual("X5", self.car.model)

        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        self.assertEqual("X5", self.car.model)

    def test_model_setter_successfully_changed(self):
        self.assertEqual("X5", self.car.model)

        self.car.model = "Q7"
        self.assertEqual("Q7", self.car.model)

    def test_fuel_consumption_setter_raises(self):
        self.assertEqual(8.4, self.car.fuel_consumption)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        self.assertEqual(8.4, self.car.fuel_consumption)

    def test_fuel_consumption_setter_successfully_changed(self):
        self.assertEqual(8.4, self.car.fuel_consumption)

        self.car.fuel_consumption = 1

        self.assertEqual(1, self.car.fuel_consumption)

    def test_fuel_capacity_setter_raises(self):
        self.assertEqual(68, self.car.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        self.assertEqual(68, self.car.fuel_capacity)

    def test_fuel_capacity_setter_successfully_changed(self):
        self.assertEqual(68, self.car.fuel_capacity)

        self.car.fuel_capacity = 62

        self.assertEqual(62, self.car.fuel_capacity)

    def test_fuel_amount_setter_raises(self):
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

        self.assertEqual(0, self.car.fuel_amount)

    def test_fuel_amount_setter_amount_changed(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.fuel_amount = 100

        self.assertEqual(100, self.car.fuel_amount)

    def test_refuel_raises(self):
        self.assertEqual(0, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-2)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_successfully_refueled(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual(68, self.car.fuel_capacity)

        self.car.refuel(60)
        self.assertEqual(60, self.car.fuel_amount)

        self.car.refuel(10)
        self.assertEqual(68, self.car.fuel_amount)

    def test_drive_raises(self):
        self.car.refuel(2)
        self.assertEqual(2, self.car.fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.drive(40)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

        self.assertEqual(2, self.car.fuel_amount)

    def test_drive_successfully_driven(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

        self.car.drive(40)

        self.assertEqual(6.64, self.car.fuel_amount)


if __name__ == "__main__":
    unittest.main()



