# Import abstract base class
from abc import ABC

# Abstract class


class Inhabitant(ABC):
    # Class attribute
    MAX_ENERGY = 100

    # Initialiser
    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    # Methods
    def __repr__(self):
        return f"name={self.name}, age={self.age}, energy={self.energy}"

    def __str__(self):
        return f"The name of this inhabitant is {self.name}. Their age is {self.age} and their energy is {self.energy}"

        # Method to increase age
    def grow(self):
        self.age += 1

    # Method to increase energy
    def eat(self, amount):
        if (self.energy + amount) <= Inhabitant.MAX_ENERGY:
            self.energy = self.energy + amount
        else:
            print("Too full to eat that!")

    # Method to reduce energy due to distance
    def move(self, distance):
        if (self.energy - distance) > 0:
            self.energy = self.energy - distance
        else:
            print("Not enough energy to move that far.")
