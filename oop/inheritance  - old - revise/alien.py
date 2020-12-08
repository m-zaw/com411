from abc import ABC, abstractmethod
from inhabitant import Inhabitant
from jetpack import Jetpack
from laser import Laser


class Alien(Inhabitant):

    def __init__(self):
        super().__init__()
        self.technology = []

    def pickup(self):
        pass

    def drop(self):
        pass
