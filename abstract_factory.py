# from abc import ABC, abstractmethod
#
# # Abstract Product
# class Transport(ABC):
#     @abstractmethod
#     def deliver(self):
#         pass
#
# # Concrete Products
# class Truck(Transport):
#     def deliver(self):
#         return "Delivering by truck"
#
# class Ship(Transport):
#     def deliver(self):
#         return "Delivering by ship"
#
# class Airplane(Transport):
#     def deliver(self):
#         return "Delivering by airplane"
#
# # Creator (Abstract Factory)
# class Logistics(ABC):
#     @abstractmethod
#     def create_transport(self):
#         pass
#
# # Concrete Creators
# class RoadLogistics(Logistics):
#     def create_transport(self):
#         return Truck()
#
# class SeaLogistics(Logistics):
#     def create_transport(self):
#         return Ship()
#
# class AirLogistics(Logistics):
#     def create_transport(self):
#         return Airplane()
#
# # Client code
# if __name__ == "__main__":
#     road_logistics = RoadLogistics()
#     transport = road_logistics.create_transport()
#     print(transport.deliver())  # Output: Delivering by truck
#
#     sea_logistics = SeaLogistics()
#     transport = sea_logistics.create_transport()
#     print(transport.deliver())  # Output: Delivering by ship
#
#     air_logistics = AirLogistics()
#     transport = air_logistics.create_transport()
#     print(transport.deliver())  # Output: Delivering by airplane
