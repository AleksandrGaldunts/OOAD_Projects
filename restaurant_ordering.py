from abc import ABC,abstractmethod
class MenuOperation(ABC):

    @abstractmethod
    def view_menu(self):
        ...

    @abstractmethod
    def view_order_history(self):
        ...

    @abstractmethod
    def place_order(self, customer, ordered_dishes):
        ...
class Menus(MenuOperation):
    menu = {}
    order_history = []

    def __init__(self,dishes:list,prices:list):
        for i in range(len(dishes)):
            self.menu[dishes[i]] = prices[i]

    def view_menu(self):
        return self.menu

    def view_order_history(self):
        return self.order_history

    def place_order(self, customer, ordered_dishes):
        new_order = Orders(customer, ordered_dishes)
        new_order.calculate_total_price()
        self.order_history.append(new_order)
        return new_order
class Dish(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Appetizer(Dish):
    def __init__(self, name, price):
        super().__init__(name, price)

class Entree(Dish):
    def __init__(self, name, price):
        super().__init__(name, price)
class Customer:
    def __init__(self,name,contact_info):
        self.name = name
        self.contact_info = contact_info

    def view_menu(self, menu):
        return menu.view_menu()

    def place_order(self, menu, ordered_dishes):
        return menu.place_order(self, ordered_dishes)

    def view_order_history(self, menu):
        return menu.view_order_history()

class Orders:
    def __init__(self,customer:Customer,ordered_dishes:list):
        self.total_price = 0
        self.customer = customer
        self.ordered_dishes = ordered_dishes

    def calculate_total_price(self):
        for dish in self.ordered_dishes:
            self.total_price += Menus.menu[dish]

    def __str__(self):
        return f"Order for {self.customer.name}: {self.ordered_dishes}, Total Price: {self.total_price}"

my_menu = Menus(["karaq", "panir"], [200, 150])

customer1 = Customer("ALIK", "098620852")
print("Menu:")
print(customer1.view_menu(my_menu))


order1 = customer1.place_order(my_menu, ["karaq", "panir"])
print(order1)

for order in customer1.view_order_history(my_menu):
    print(order)

customer2 = Customer("Vazgen", "098625452")
print(customer2.view_menu(my_menu))

order2 = customer2.place_order(my_menu, ["panir"])
print(order2)

for order in customer2.view_order_history(my_menu):
    print(order)


