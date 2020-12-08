# The Inhabitant class will be the super class for Human and Robot, it will share common
# methods between them which are similar to the ones from last week.
class Inhabitant:
    MAX_ENERGY = 100

    # When specifying a global variable inside __init__, we'd do something like MAX_ENERGY=100
    def __init__(self, name="Inhabitant", age=0):
        self.name = name
        self.age = age
        self.energy = Inhabitant.MAX_ENERGY

    def eat(self, amount):
        temp = self.energy + amount

        if (temp > 100):
            self.energy = 100
            print("I can't eat more, I'm full!".format)
        else:
            self.energy = temp
            print("That was yummy! My energy is now at {}!".format(self.energy))

    def grow(self):
        self.age += 1
        print("It's my birthday! I'm now {} years old.".format(self.age))

    def move(self, distance):
        temp = self.energy - distance

        if (temp < 0):
            self.energy = 0
            print("I couldn't make it!")
        else:
            self.energy = temp
            print("I made it to the destination! My energy is now {}".format(self.energy))

    def __str__(self):
        return self.name

    def __repr__(self):
        return "inhabitant=(name={}, age={}, energy={})".format(self.name, self.age, self.energy)


if (__name__ == "__main__"):
    test = Inhabitant("test", 10)
    print(test)
    print(repr(test))
