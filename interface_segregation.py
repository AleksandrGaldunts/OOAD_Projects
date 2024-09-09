# Interface Segregation principe
"""
    Հարկավոր է ստեղծել նեղ սպեցիֆիկացված interface֊ներ  հստակ սահմանված կոնկրետ client֊ի համար։
    client֊ները չպետք է կախում ունենան այն interface֊ներից, որոնցից նրանք չեն օգտվում։
"""
# Խախտում
from abc import ABC, abstractmethod


class MultiFunctionDevice(ABC):
    @abstractmethod
    def print_content(self, content):
        pass

    @abstractmethod
    def scan_content(self, content):
        pass


class PrinterScanner(MultiFunctionDevice):
    def print_content(self, content):
        print(f"Printing: {content}")

    def scan_content(self, content):
        print(f"Scanning: {content}")


# ճիշտ իրականացում
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_content(self, content):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_content(self, content):
        pass


class OnlyPrinter(Printer):
    def print_content(self, content):
        print(f"Printing: {content}")


class OnlyScanner(Scanner):
    def scan_content(self, content):
        print(f"Scanning: {content}")
