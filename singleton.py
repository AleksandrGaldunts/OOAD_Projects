#   Singleton

"""
    Դա creational design pattern է, որը երաշխավորում է, որ class ֊ը ունենալու է միայն instance։
    Այն հնարավորություն է տալիս կառավարել shared resource֊ները՝ օրինակ database:
"""


class Single:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonMeta):
    ...


"""
    Այս design pattern֊ը խախտում է SRP֊ն Solid-ի քանի որ ստեղծվում է 1 օբյեկտ,
     այսինքն գոյություն ունի մեկ օբյեկտ և ցանկացած բան փոխելուց կփոխի բոլոր տեղերում։

"""

