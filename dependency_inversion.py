# Dependency inversion principe
"""
    Dependency inversion principe֊ի  մեջ ասվում է որ բարձր level-ի մոդուլը չպետք է կախված լինի՝
     ավելի ցածր level֊ի մոդուլից, այլ երկուսն ել պետք է կախված լինեն աբստրակցիայից։
     Նաև աբստրիակցիաները չպետք է կախված լինեն դետալներից, դետալները պետք է կախված լինեն աբստրակցիային։
"""

from abc import ABC, abstractmethod
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        ...

    @abstractmethod
    def turn_off(self):
        ...
class BlueLight(Switchable):  # Low-level module
    def turn_on(self):
        print("Blue light turn on")

    def turn_off(self):
        print("Blue light turn off")
class Switch:  # High-level module
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()
if __name__ == "__main__":
    blue = BlueLight()
    switch = Switch(blue)
    switch.operate()
