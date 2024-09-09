# # # # from abc import ABC, abstractmethod
#
# # # # class Vehicle(ABC):
# # # #   def __init__(self, speed = 0):
# # # #     self.speed = 0
#
# # # #   @abstractmethod
# # # #   def adjust_speed(self, amount):
# # # #     ...
#
#
#
# # # # class Car(Vehicle):
# # # #   def adjust_speed(self, amount):
# # # #     self.speed += amount
# # # #     print(f"Speed adjusted to {self.speed} km/h")
#
# # # # class SportCar(Vehicle):
# # # #   def adjust_speed(self, amount):
# # # #     self.speed += 10
# # # #     self.speed += amount
# # # #     print(f"Speed adjusted to {self.speed} km/h")
#
#
# # # # class Airplane(Vehicle):
# # # #   def adjust_speed(self, amount):
# # # #     self.speed += amount
# # # #     print(f"Speed adjusted to {self.speed} km/h")
#
# # # # from typing import List
#
# # # # def client(vehicle: List[Vehicle]):
# # # #   for i in vehicle:
# # # #     i.adjust_speed(10)
#
#
# # # # vehicles = [Car(), SportCar(38), Airplane(300)]
#
# # # # class Chlp:
# # # #   def adjust_speed(self, x):
# # # #     raise ValueError("sssss")
#
# # # # chlp = Chlp()
# # # # vehicles.append(chlp)
# # # # client(vehicles)
#
#
# # # # S - Single Responsibilty principle
#
# # # #  a class should have just one reason to change
#
# # # # Bad
#
# # # class User:
# # #   def __init__(self, username, email):
# # #     self.username = username
# # #     self.email = email
#
# # #   def change_email(self, new_mail):
# # #     self.email = new_mail
# # #     self.send_email(new_mail, "Email change", "Your email changed successfully")
#
# # #   def send_email(self, email, subject, message):
# # #     print(f"Sending email to {email} with subject: {subject} and message: {message}")
#
#
# # # class User:
# # #   def __init__(self, username, email):
# # #     self.username = username
# # #     self.email = email
#
# # #   def change_email(self, new_mail):
# # #     self.email = new_mail
# # #     EmailSender.send_email(user.email, 'Change Email', 'Your email changed successfully')
#
#
# # # class EmailSender:
# # #   @staticmethod
# # #   def send_email(email, subject, message):
# # #     print(f"Sending email to {email} with subject: {subject} and message: {message}")
#
#
#
# # # user = User("Bob888", "email@example.com")
#
# # # user.change_email('bob8@example.com')
#
#
# # #  Open-closed principle
#
# # #  բաց է ընդլայման համար։ բայց փակ փոփոխոխությունների համար
#
# # final
#
# from typing import final
#
# # 1.
# # @final
# # class Base:
# #   pass
# #
# # class Derived(Base):
# #   pass
# #
# # b = Derived()
#
# # 2. method
# # class Base:
# #   @final
# #   def method(self)->None:
# #     print('Base')
#
# # class Derived(Base):
# #   def method(self)->None:
# #     print('Derived')
#
# # d = Derived()
# # d.method()
#
# # class FinalMeta(type):
# #   def __new__(mcls, name, bases, cls_dict, **kwargs):
# #     print(f'class bases: {bases}')
# #     print(f'class name: {name}')
# #     # for item in bases:
# #     #   if isinstance(item, FinalMeta):
# #     #     raise TypeError(f"Type {item.__name__} is not an acceptable base type")
# #     return super().__new__(mcls, name, bases, cls_dict)
# #
# # class FinalClass(metaclass=FinalMeta):
# #   pass
# #
# # class SecondClass(FinalClass, metaclass= FinalMeta):
# #   pass
# #
# # ThirdClass = FinalMeta('ThirdClass', (SecondClass, FinalClass), {})
# #
# #
# # class Order:
# #   def __init__(self, line_items, shipping_type):
# #     self.line_items = line_items
# #     self.shipping_type = shipping_type
# #
# #   def getTotal(self):
# #     'Calcualting total cost of line items'
# #
# #     return sum(item['price'] * item['quantity'] for item in self.line_items)
# #
# #   def get_total_weight(self):
# #     return sum(item['weight'] + item['quantity'] for item in self.line_items)
# #
# #   def get_shipping_cost(self):
# #     if self.shipping == 'ground':
# #       if self.getTotal() > 100:
# #         return 0
# #
# #       return max(10, self.get_total_weight() * 1.5)
# #
# #     elif self.shipping_type == 'air':
# #       return max(20, self.get_total_weight() * 3)
# #
# #
# # #  Good
# # from abc import ABC, abstractmethod
# # class Shipping(ABC):
# #
# #   @abstractmethod
# #   def get_cost(self, order: Order):
# #     ...
# #
# # class Ground(Shipping):
# #   def get_cost(self, order: Order):
# #     # nuyn verevi gortsoghutyun
# #     pass
# #
#
# class FinalMeta(type):
#     def __new__(cls, name, bases, namespace):
#         for base in bases:
#             if isinstance(base, FinalMeta):
#                 raise TypeError(f"Cannot inherit from final class '{base.__name__}'")
#         return super().__new__(cls, name, bases, namespace)
#
#     def __init__(self, name, bases, namespace):
#         super().__init__(name, bases, namespace)
#
#     def __init_subclass__(cls, *args, **kwargs):
#         raise TypeError(f"Cannot subclass final class '{cls.__name__}'")
#
# class FinalClass(metaclass=FinalMeta):
#     def __init__(self):
#         pass
#
# # Attempting to subclass FinalClass will raise an error
# class Subclass(FinalClass):
#     pass
#

#
# """Custom final metaclasses"""
#
#
# class FinalInh(type):
#     """Metaclass for preventing inheritance(runtime)"""
#
#     def __new__(mcls, name, bases, cls_dict, **kwargs):
#         for base in bases:
#             if isinstance(base, FinalInh):
#                 raise TypeError(f'Cannot inherit from class {name}!')
#         return super().__new__(mcls, name, bases, cls_dict)
#
#
# class FinalOvr(type):
#     """Metaclass for preventing attribute overriding(runtime)"""
#
#     def __new__(mcls, name, bases, cls_dict, **kwargs):
#         for base in bases:
#             for attr in cls_dict.keys():
#                 if (
#                     not attr in ('__module__', '__qualname__') and
#                     attr in base.__dict__.keys()
#                 ):
#                     raise TypeError(f'Cannot override attribute {attr}!')
#         return super().__new__(mcls, name, bases, cls_dict, **kwargs)


# from typing import Protocol, List,runtime_checkable
# @runtime_checkable
# class Sortable(Protocol):
#     def sort(self) -> List[int]:
#         ...
#
# class SomeClass:
#     def sort(self) -> List[int]:
#         # Implementation of sort method
#         return sorted([3, 1, 2])
#
# def sort_and_print(obj: Sortable) -> None:
#     sorted_list = obj.sort()
#     print(sorted_list)
#
# # SomeClass implements the Sortable protocol
# instance = SomeClass()
# sort_and_print(instance)  # This will work because SomeClass implements the Sortable protocol
# print(isinstance(SomeClass,Sortable))


class Protocol:
    def __init__(self, **methods):
        self.methods = methods

    def __call__(self, cls):
        for method_name, method in self.methods.items():
            if not hasattr(cls, method_name):
                setattr(cls, method_name, method)
        return cls

def implements_protocol(obj, protocol):
    for method_name in protocol.methods.keys():
        if not hasattr(obj, method_name) or not callable(getattr(obj, method_name)):
            return False
    return True


# Define a protocol using Protocol class and @Protocol decorator
@Protocol(sort=lambda self: NotImplemented)
class Sortable:
    pass

# Define a class that implements the Sortable protocol
class SomeClass:
    def sort(self):
        print("Sorting...")

# Define another class that does not implement the Sortable protocol
class AnotherClass:
    pass

# Create an instance of the class that implements the Sortable protocol
obj1 = SomeClass()
# Check if the instance implements the Sortable protocol
print(implements_protocol(obj1, Sortable))  # Output: True

# Create an instance of the class that does not implement the Sortable protocol
obj2 = AnotherClass()
# Check if the instance implements the Sortable protocol
print(implements_protocol(obj2, Sortable))  # Output: False