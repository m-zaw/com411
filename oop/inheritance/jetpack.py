from tech import Tech


class Jetpack(Tech):
    def __init__(self):
        super().__init__()

    def activate(self):
        print("Jetpack activated!")

    def fly(self):
        print("Flying with jetpack!")

    def deactivate(self):
        print("Jetpack deactivated!")
