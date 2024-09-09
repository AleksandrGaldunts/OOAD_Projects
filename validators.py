from abc import ABC, abstractmethod
import re
from datetime import datetime


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        delattr(instance, self.name)

    @abstractmethod
    def validate(self, value) -> None:
        ...


class Email(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'Expected {value} to be a str!')
        email_pattern = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        if not email_pattern.fullmatch(value):
            raise ValueError('Invalid email pattern!')

class String(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'Expected {value} to be a str!')
        if value == '':
            raise ValueError('Passed value cannot be an empty string!')

class Integer(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError(f'Expected {value} to be an int!')
        if value <= 0:
            raise ValueError('Passed value cannot be negative!')


class Number(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value} to be an int or float!')
        if value <= 0:
            raise ValueError('Passed value cannot be negative!')


class DateTime(Validator):
    def validate(self, value) -> None:
        if not isinstance(value, datetime):
            raise TypeError(f'Expected {value} to be a datetime type!')