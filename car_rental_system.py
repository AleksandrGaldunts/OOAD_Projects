from __future__ import annotations
from validators import Email,Integer,String
from abc import ABC,abstractmethod

class Car(ABC):
    cars = {}
    def __init__(self, make: list, model: list, rental_price: list):
        self.model = model
        self.rental_price = rental_price
        self.make = make
        self.available = True
        for i in range(len(model)):
            self.cars[model[i]] = [rental_price[i], make[i]]

    def __repr__(self):
        return f"{self.make} {self.model}  {self.rental_price}"

    @abstractmethod
    def car_type(self):
        ...

class LuxuryCar(Car):
    def car_type(self):
        return "LuxuryCar"

class EconomyCar(Car):
    def car_type(self):
        return "EconomyCar"

class Customer:
    name = String()
    contact_info = Email()

    def __init__(self,name:str,contact_info:Email):
        self.name = name
        self.contact_info = contact_info
        self.rental_history = []

    def search_car(self):
        return {model: details for model, details in Car.cars.items() if Car.cars[model][0]}

    def rent_car(self, model, rental_duration):
        if model in Car.cars and Car.cars[model][0] > 0:
            rental = Rental(self, model, rental_duration)
            self.rental_history.append(rental)
        else:
            return False

    def return_car(self, model):
        if model in Car.cars:
            Car.cars[model][0] += 1


class RentalOperation(ABC):
    @abstractmethod
    def view_rental_history(self):
        ...

class Rental(RentalOperation):

    rental_history = []

    rental_duration = Integer()
    car_model = String()

    def __init__(self, customer: Customer, car_model: str, rental_duration: int):
        self.customer = customer
        self.car_model = car_model
        self.rental_duration = rental_duration
        self.record_rental()

    def record_rental(self):
        return self.rental_history.append((self.customer.name, self.car_model, self.rental_duration))

    def view_rental_history(self):
        return self.rental_history

car = LuxuryCar(['BMW', 'Audi'], ['7 Series', 'A8'], [300, 350])
customer = Customer("Alik","alik.0208@mail.ru")
customer2 = Customer("vazgen","vazgen@mail.ru")
rental = Rental(customer,"bmw",5)

available_cars = customer.search_car()
print(available_cars)
customer.rent_car("bmw",4)
customer.return_car("mercedes")


rental2 = Rental(customer2,"mercedes",7)
print(rental.rental_history)
print(car.cars)
print(car)




