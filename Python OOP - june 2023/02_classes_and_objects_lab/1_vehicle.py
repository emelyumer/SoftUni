class Vehicle:
    def __init__(self, mileage, max_speed=150, gadgets=list()):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = gadgets



car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)