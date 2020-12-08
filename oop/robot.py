class Robot:

    # class attribute
    laws = "Protect, Obey and Survive"

    # class (constant) attribute
    MAX_ENERGY = 100

    # A static method
    @staticmethod
    def the_laws():
        print(Robot.laws)

    # An initialiser (special instance method)
    def __init__(self, name="Robot", age=0):

        # An instance attribute
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

    # An instance method
    def display(self):
        print(f"I am {self.name}")

    def eat(self, amount):
        potential_energy = self.energy + amount
        if (potential_energy > Robot.MAX_ENERGY):
            self.energy = Robot.MAX_ENERGY
            return potential_energy - self.energy
        else:
            self.energy = potential_energy
            return 0

    def grow(self):
        self.age += 1

    def move(self, distance):
        potential_energy = self.energy - distance
        if (potential_energy < 0):
            self.energy = 0
            return self.energy - abs(potential_energy)
        else:
            self.energy = potential_energy
            return 0


if (__name__ == "__main__"):
    robot = Robot()
    Robot.the_laws()
    print(repr(robot))
    robot.move(10)
    print(repr(robot))
    robot.eat(5)
    print(repr(robot))
    robot.eat(20)
    print(repr(robot))
