from abc import ABC, abstractmethod


class Inhabitant(ABC):

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Inhabitant"
        self.age = 0
        self.energy = Inhabitant.MAX_ENERGY

    def grow(self):
        self.age += 1

    def eat(self, eat):

        if (self.energy + eat) > 100:
            print("You already have enough energy!")
        else:
            self.energy = self.energy + eat

    def move(self, distance):
        if self.energy > distance:
            self.energy = self.energy - distance
        else:
            print("Eat something. Your energy is low.")
