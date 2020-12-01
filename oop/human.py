class Robot:

    laws = "Protect, Obey and Survive"

    def the_laws(self):
        print(Robot.laws)

    def __init__(self):

        self.name = "Robot"
        self.age = 0

    def display(self):
        print(f"I am {self.name}")


if (__name__ == "__main__"):
    robot = Robot()
    robot.display()


class Human:

    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")


if (__name__ == "__main__"):
    human = Human()
    human.display()
