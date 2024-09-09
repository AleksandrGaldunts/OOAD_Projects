import random
from abc import ABC,abstractmethod
class StringValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if instance is None:
            return self
        if not isinstance(value, str):
            raise ValueError("Must be String")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, "")

class Property(ABC):
    address  = StringValue()

    def __init__(self,address:str,price:int,features:list):
        self.address = address
        self.price = price
        self.features = features

    def __str__(self):
        return f'Property at the address {self.address}, price {self.price}, features {self.features}'

class Residental(Property):
    pass

class Commercial(Property):
    pass


class Client:

    name =  StringValue()
    contact_info = StringValue()

    def __init__(self,name:str,contact_info:str):
        self.name = name
        self.contact_info = contact_info
        self.rented_history  = []

    def purchase_properties(self,property:Property):
        self.property=property
        self.rented_history.append(property)

    def __str__(self):
        return f'name : {self.name} contact info  : {self.contact_info}'


class Agent:
    name = StringValue()
    contact_info = StringValue()

    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.properties = []
        self.clients = []

    def add_to_listing(self, property: Property):
        self.properties.append(property)

    def remove_from_listing(self, property: Property):
        self.properties.remove(property)

class RealEstateOperations:

    def search_properties(self,client:Client,agent:Agent):
        print(f'{random.choice(agent.properties)} property found for {client}')



cl=Client('Bobby','08888888')
ag=Agent('Gabriel','097000009')
reo=RealEstateOperations()
residental=Residental('Ler Kamsar','300000','dush chka')
ag.add_to_listing(residental)
for i in ag.properties:
    print(i)
cl.purchase_properties(residental)
reo.search_properties(cl,ag)



