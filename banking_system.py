from abc import ABC, abstractmethod
from datetime import datetime

class Customer:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def update_address(self, new_address):
        self.address = new_address

    def update_contact_info(self, new_contact_info):
        self.contact_info = new_contact_info

class Account(ABC):
    def __init__(self, id_card, balance, interest_rate, owner: Customer):
        self.id_card = id_card
        self.balance = balance
        self.interest_rate = interest_rate
        self.owner = owner

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def get_balance(self):
        return self.balance

class SavingAccount(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, id_card, balance, interest_rate, owner, overdraft_limit):
        super().__init__(id_card, balance, interest_rate, owner)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

class Transaction:
    def __init__(self, account: Account, transaction_type, amount, date_time: datetime):
        self.account = account
        self.transaction_type = transaction_type
        self.amount = amount
        self.date_time = date_time

    def execute(self):
        if self.transaction_type == 'deposit':
            self.account.deposit(self.amount)
        elif self.transaction_type == 'withdrawal':
            self.account.withdraw(self.amount)


customer = Customer("ALIK", "AVAN", "098620852")
customer.update_address("SILACHI")

ca = CheckingAccount("654184651684", 6000, 0.05, customer, 2000)

print(f"Customer Name: {customer.name}")
print(f"Customer Address: {customer.address}")
print(f"Checking Account Balance: {ca.get_balance()}")

transaction1 = Transaction(ca, 'deposit', 500, datetime.now())
transaction1.execute()

print(ca.get_balance())

transaction2 = Transaction(ca, 'withdrawal', 1000, datetime.now())
transaction2.execute()

print(ca.get_balance())
