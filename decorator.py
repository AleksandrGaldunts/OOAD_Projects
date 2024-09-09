# Decorator design pattern


"""
Decorator֊ը structural design pattern է, որը մեզ  հնարավորություն է տալիս դինամիկորեն ավելացնել նոր behavior:

"""

class Coffee:
    def cost(self):
        ...

class SimpleCofee(Coffee):
    def cost(self):
        return 500

class MilkDecorator(Coffee):
    def __init__(self, cofee):
        self._coffee = cofee
    def cost(self):
        return self._coffee.cost() + 250

simple = SimpleCofee()
milk = MilkDecorator(simple)
print(milk.cost())
print(simple.cost())