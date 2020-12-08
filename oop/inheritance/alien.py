from jetpack import Jetpack
from laser import Laser
from inhabitant import Inhabitant


class Alien(Inhabitant):
    def __init__(self, name="Alien"):
        super().__init__(name)
        self.technology = []

    def pickup(self, tech):
        self.technology.append(tech)

    def drop(self, tech):
        self.technology.remove(tech)

    def __repr__(self):
        return f"technology = {self.technology}"

    def __str__(self):
        return f"Alien has {self.technology} technology available."


# Testing area
if (__name__ == "__main__"):
    alien = Alien("Bob")
    jetpack = Jetpack()
    laser = Laser()

    alien.pickup(jetpack)
    alien.pickup(laser)
    print(alien)

    jetpack.activate()
