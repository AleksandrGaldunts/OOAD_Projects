# # strategy design pattern
#
# """
#     Strategy-ն behavioral design pattern է, որը հնարավորություն է տալիս սահմանել ալգորիթմներ (ալգորիթմների ընտանիք),
#     դրանից յուրաքանչյուրը դնել (տանել) առանձին class֊ի մեջ և դրանց օբյեկտները դարձնել փոխանակելի:
#     (ծրագրի կատարման ընթացքում ալգորիթմը կարող են փոխանակվել):
# """
# from abc import ABC,abstractmethod
# class PaymentStrategy(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         ...
# class CreditCardPayment(PaymentStrategy):
#     def pay(self, amount):
#         print(f"{amount} using Card")
# class PaypalPayment(PaymentStrategy):
#     def pay(self, amount):
#         print(f"{amount} using Paypal")
# class ShoppingCard:
#     def __init__(self, paym_strategy):
#         self.paym_strategy = paym_strategy
#     def checkout(self, amount):
#         self.paym_strategy.pay(amount)
# credcard = CreditCardPayment()
# cart1 = ShoppingCard(credcard)
# cart1.checkout(10)
#
# paypal = PaypalPayment()
# cart2 = ShoppingCard(paypal)
# cart2.checkout(50)


from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} using Card")

class PaypalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} using Paypal")

class ShoppingCard:
    def __init__(self, paym_strategy):
        self.paym_strategy = paym_strategy

    def checkout(self, amount):
        self.paym_strategy.pay(amount)

credcard = CreditCardPayment()
cart1 = ShoppingCard(credcard)
cart1.checkout(10)

paypal = PaypalPayment()
cart2 = ShoppingCard(paypal)
cart2.checkout(50)

