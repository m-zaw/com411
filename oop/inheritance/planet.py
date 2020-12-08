from human import Human
from robot import Robot

# Define Planet class


class Planet:
    # Instance variables
    def __init__(self):
        self.inhabitants = []

    # Instance method for adding inhabitants
    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    # Instance method for removing inhabitants
    def remove_inhabitant(self, inhabitant):
        self.inhabitants.remove(inhabitant)

# Magic methods for displaying data
    def __repr__(self):
        return f"planet(inhabitants= {self.inhabitants})"

    def __str__(self):
        return f"There are {len(self.inhabitants)} inhabitants on this planet."


# Testing area
if (__name__ == "__main__"):
    planet = Planet()

    darren = Human("Darren")
    beep = Robot("Beep")
    bop = Robot("Bop")
    bender = Robot("Bender")

    planet.add_inhabitant(darren)
    print(planet)
    planet.add_inhabitant(beep)
    print(planet)

    planet.add_inhabitant(bop)
    planet.add_inhabitant(bender)
    print(planet)

    planet.remove_inhabitant(bender)
    planet.remove_inhabitant(darren)
    print(planet)
