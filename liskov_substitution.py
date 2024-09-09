# Liskov Substitution Principe
"""
    Այնտեղ որտեղ սպասում ենք բազային տիպի օբյեկտ, կարող ենք փոխանցել նաև subclass֊ի օբյեկտ և պետք է նույնությամբ աշխատի։
    1) argument type of subclass (Base type)
    Base class֊ի արգումենտն ֆունկցիաները պետք է ստանան նույն տիպի արգումենտներ։
    2) return of type classes
    Եթե ծնողի ֆունկցիան վերադարձնում է օրինակ str էնէլ պիտի վերադարձնի str
    3) exception in subclass the same
    erornery նույնը պետքա ըլնեն
    4) envoriant
    այն պայմանները, որոնք ճիշտ են base class֊ի օբյեկտի համար, չպետք է խախտվեն subclass֊ում։
"""
#   Խախտում
class Bird:
    def fly(self):
        return "Flying high!"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")
#   Ճիշտ իրականացում
class Bird:
    def move(self):
        return "Moving!"
class FlyingBird(Bird):
    def move(self):
        return "Flying high!"
class Penguin(Bird):
    pass
