from tech import Tech


class Jetpack(Tech):

    def __init__(self):
        super().__init__()

    def fly(self, speed):
        if self.active == True:
            print(f"Jetpack activated! Current speed: {speed}mph.")
        else:
            print("Power ON your jetpack.")
