class Robot:

    LAWS = "Protect, Obey and Survive"

    def the_laws():
        print(Robot.LAWS)

    def __init__(self, name="Robot", age=0):

        self.name = name
        self.age = age

    def display(self):
        print("I am {}!".format(self.name))

    def grow(self):
        self.age += 1

    def eat(self, amount):
        print("I'm a robot, I cannot eat {} food.".format(amount))

    def move(self, distance):
        print("Moved {}, I'm a robot with infinite energy.".format(distance))

    def __repr__(self):
        return "robot(name={}, age={})".format(self.name, self.age)

    def __str__(self):
        return self.name


if (__name__ == "__main__"):
    beep = Robot("Beep")
    beep.display()

    Robot.the_laws()

    print(beep)
