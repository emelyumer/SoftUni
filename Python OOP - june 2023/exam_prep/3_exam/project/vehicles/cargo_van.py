from project.vehicles.base_vehicle import BaseVehicle


class CargoVan (BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float = 180.00):
        super().__init__(brand, model, license_plate_number, max_mileage)

    def drive(self, mileage: float):
        self.battery_level -= (round(mileage / self.max_mileage * 100) + 5)
        return self.battery_level
