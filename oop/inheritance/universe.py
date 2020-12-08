from planet import Planet
import random


class Universe():

    def __init__(self):
        self.planets = []

    def generate(self):
        planet = Planet()
        for _ in range(random.randrange(1, 4)):
            planet.add_human(str(random.randrange(1, 500)))
        for _ in range(random.randrange(1, 4)):
            planet.add_robot(str(random.randrange(1, 500)))

        self.planets.append(planet)
        print(self.planets[0])

    def show_populations(self):
        print(self.planets)


if __name__ == "__main__":
    uni = Universe()
    uni.generate()
    uni.show_populations()
