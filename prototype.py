"""
    prototype֊ը creational design pattern է, որը թույլ է տալիս պատճենել գոյություն ունեցող օբյեկտները՝ առանց ձեր կոդը կախվածության մեջ դնելով դրանց դասերից:

"""

import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return f"Type: ConcretePrototype1, Field: {self.field}"

class ConcretePrototype2(Prototype):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return f"Type: ConcretePrototype2, Field: {self.field}"

# Usage
prototype1 = ConcretePrototype1("Field1")
prototype2 = ConcretePrototype2("Field2")

cloned_prototype1 = prototype1.clone()
cloned_prototype2 = prototype2.clone()

print(prototype1)  # Original
print(cloned_prototype1)  # Cloned

print(prototype2)  # Original
print(cloned_prototype2)  # Cloned
