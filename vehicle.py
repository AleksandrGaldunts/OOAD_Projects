class Vehicle:
    __vehicle_count = 0

    def __init__(self, make, model):
        Vehicle.increment_vehicle_count()
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"

    @classmethod
    def increment_vehicle_count(cls):
        cls.__vehicle_count += 1

    @classmethod
    def get_vehicle_count(cls):
        return cls.__vehicle_count

class Car(Vehicle):
    def __init__(self,make,model):
        super().__init__(make,model)
        self.number_of_wheels = 4
    def __repr__(self):
        return f'This car is made in {self.make},and model is {self.model} and number of wheels is by default {self.number_of_wheels}'

    def start_engine(self):
        return "Car engine started"


class ElectricVehicle:
    def __init__(self,battery_capacity):
        self.battery_capacity = battery_capacity


class ElectricCar(Car,ElectricVehicle):
    pass

print(ElectricCar.mro())
print(ElectricCar.__mro__)

print(Vehicle.get_vehicle_count())
ob = Vehicle(16,'bmw')
print(Vehicle.get_vehicle_count())
ob2 = Car(2020,"mercedes")
print(ob2)
print(ob.start_engine())

# print(ob.make)
# print(ob.model)
# print(ob2.number_of_wheels)

print(Vehicle.get_vehicle_count())
ob3 = Vehicle(16,'bmw')
print(Vehicle.get_vehicle_count())
ob4 = Vehicle(16,'bmw')
print(Vehicle.get_vehicle_count())




