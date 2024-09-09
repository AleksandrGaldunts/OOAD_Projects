from __future__ import annotations
from validators import Email, Integer, String
from abc import ABC, abstractmethod


class Service:
    def __init__(self):
        self.products = []


class Product:
    name = String()
    price = Integer()
    description = String()

    def __init__(self, name: str, price: int, description: str):
        self.name = name
        self.price = price
        self.description = description
        self.reviews = []

    def __repr__(self):
        return f"product name {self.name} price:{self.price} description:{self.description}"


class ElectronicProduct(Product):
    pass


class ClothingProduct(Product):
    pass


class Order:
    quantity = Integer()
    price = Integer()
    total = Integer()

    def __init__(self, customer: Customer, *products: Product):
        self.customer = customer
        self.product = products
        self.total = sum(product.price for product in products)

    def __repr__(self):
        return f"Customer:{self.customer},Products:{self.product}"


class Customer:
    name = String()
    contact_info = Email()

    def __init__(self, name: str, contact_info: Email):
        self.name = name
        self.contact_info = contact_info
        self.order_history = []

    def search_product(self, product: Product, service: Service):
        for pr in service.products:
            if pr == product:
                print("Successfuly found")
                return
        print("not founded")

    def purchase_product(self, product: Product, service: Service):
        if product in service.products:
            order = Order(self, product)
            self.order_history.append(order)
            print(f"purchasing {product} product ")
        else:
            print("There is no product like that")

    def view_order_history(self):
        for i in self.order_history:
            print(i)

    def leave_review(self, product: Product, review: str):
        product.reviews.append(review)

    def __repr__(self):
        return f"Customer name :{self.name}, contact_info:{self.contact_info}"


service = Service()

karaq = Product('karaq', 500, 'zelandakan')

service.products.append(karaq)

customer = Customer("Alik", "abc@mail.ru")

customer.search_product(karaq, service)
customer.purchase_product(karaq, service)
customer.view_order_history()
customer.leave_review(karaq, "shat lavna")
