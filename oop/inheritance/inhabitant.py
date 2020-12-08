class Inhabitant:

    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        pass

    def grow(self):
        self.age = self.age + 1

    def eat(self, amount):
        if(self.energy + amount > Inhabitant.MAX_ENERGY):
            self.energy = Inhabitant.MAX_ENERGY
        else:
            self.energy += amount

    def move(self, distance):
        potential_energy = self.energy - distance
        self.energy = max(potential_energy, 0)
