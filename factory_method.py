    # Factory Method creational

"""
    Factory Method֊ը creation design pattern է, որը մեզ հնարավորություն է տալիս ընդհանուր ինտերֆեյս օբյեկտ
    ստեղծելու համար,  superclass֊ում թույլ տալով ժառանգ կլասսներին փոխել ստեղծվող օբյեկտի տիպը։
"""
from abc import ABC, abstractmethod


class Animal(ABC):  # Abstract Product
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):  # Concrete Products

    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory(ABC):  # Concrete Creator with Factory Method
    @abstractmethod
    def create_animal(self):
        ...


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


def get_animal_sound(factory):  # Client
    animal = factory.create_animal()
    return animal.speak()


# Example usage
print(get_animal_sound(DogFactory()))  # Output: Woof!
print(get_animal_sound(CatFactory()))  # Output: Meow!
