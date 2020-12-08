from abc import ABC, abstractmethod


class Tech(ABC):

    def __init__(self):
        self.active = False

    @abstractmethod
    def activate(self):
        if self.active == False:
            print("Powering Up")
            self.active = True
        else:
            print("Already ON.")

    @abstractmethod
    def deactivate(self):
        if self.active == True:
            print("Shutting Down")
            self.active = False
        else:
            print("Power is OFF.")
