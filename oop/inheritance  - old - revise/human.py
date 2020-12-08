from abc import ABC, abstractmethod
from inhabitant import Inhabitant


class Human(Inhabitant):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def display(self):
        print("I am {} and I am {} years old, I have an energy of {}".format(
            self.name, self.age, self.energy))

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old.'

    def __repr__(self):
        return f'(name={self.name}, age={self.age},energy={self.energy})'


if (__name__ == "__main__"):
    human = Human("Harry")
    print(repr(human))
    human.move(10)
