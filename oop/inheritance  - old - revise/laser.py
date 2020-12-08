from tech import Tech


class Laser(Tech):

    MAX_RANGE = 50

    def fire(self, range):
        if self.active == True:
            if range > Laser.MAX_RANGE:
                print("Move closer. Out of range.")
            else:
                print("Pew! Pew! Pew!")
        else:
            print("Power ON your laser.")
