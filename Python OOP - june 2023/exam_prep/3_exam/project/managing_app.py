from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPE = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        exits_user = [u for u in self.users if u.driving_license_number == driving_license_number]

        if exits_user:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ManagingApp.VALID_VEHICLE_TYPE.keys():
            return f"Vehicle type {vehicle_type} is inaccessible."

        exits_vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number]
        if exits_vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = ManagingApp.VALID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        exits_route = \
            [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length == length]

        if exits_route:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        exits_route = \
            [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length < length]

        if exits_route:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        exits_route = \
            [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length > length]

        if exits_route:
            exits_route[0].is_locked = True

        new_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        road = [r for r in self.routes if r.route_id == route_id][0]

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if road.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(road.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
            return str(vehicle)

        user.increase_rating()
        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]

        sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))[:count]

        for index in range(len(sorted_damaged_vehicles)):
            sorted_damaged_vehicles[index].is_damaged = False
            sorted_damaged_vehicles[index].recharge()

        return f"{len(sorted_damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_user = sorted(self.users, key=lambda x: -x.rating)

        result = "*** E-Drive-Rent ***\n"

        result += '\n'.join([str(su) for su in sorted_user])

        return result
