from inhabitant import Inhabitant
from clothing import Clothing
from clothingsize import ClothingSize

# Define Human class


class Human(Inhabitant):

    # Initialiser
    def __init__(self, name="Human"):
        super().__init__(name)
        self.clothing = []

    # Instance method
    def display(self):
        print(f"I am {self.name}")

    # Debugging method
    def __repr__(self):
        return f"name={self.name}, age={self.age}, energy={self.energy}"

    # Print method
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old. My energy level is {self.energy}. I am wearing {self.clothing}"

    def dress(self, clothing):
        self.clothing.append(clothing)

    def undress(self, clothing):
        self.clothing.remove(clothing)


# Testing area
if (__name__ == "__main__"):

    # Human object
    human = Human()
    top = Clothing("Red", "Cotton", ClothingSize.Small)
    human.dress(top)
    print(human)
