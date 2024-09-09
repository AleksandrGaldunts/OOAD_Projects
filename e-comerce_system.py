from abc import ABC, abstractmethod

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = []

class Electronics(Product):
    pass

class Clothing(Product):
    pass

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def leave_review(self, product, review):
        product.reviews.append((self.name, review))

class OrderOperations(ABC):
    @abstractmethod
    def search_products(self, product_list, search_name):
        pass

    @abstractmethod
    def purchase_product(self, customer, product, quantity):
        pass

    @abstractmethod
    def view_order_history(self, customer):
        pass

    @abstractmethod
    def leave_review(self, customer, product, review):
        pass

class Order(OrderOperations):
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
        customer.order_history.append(self)

    def search_products(self, product_list, search_name):
        return [product for product in product_list if search_name.lower() in product.name.lower()]

    def purchase_product(self, customer, product, quantity):
        return Order(customer, product, quantity)

    def view_order_history(self, customer:Customer):
        return customer.order_history

    def leave_review(self, customer, product, review):
        customer.leave_review(product, review)


laptop = Electronics("Laptop", 1000, "gaming")
shirt = Clothing("Shirt", 20, "from cotton")
product_list = [laptop, shirt]

customer1 = Customer("Mane", "098620852")

order_ops = Order(customer1, laptop, 0)

search_results = order_ops.search_products(product_list, "laptop")
print("Search results", [product.name for product in search_results])

order = order_ops.purchase_product(customer1, laptop, 2)
print(order.product.name, "Quantity:", order.quantity, "Total price:", order.total_price)

order_ops.leave_review(customer1, laptop, "very cheap")
print("reviews for laptop", laptop.reviews)
