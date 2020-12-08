from abc import ABC, abstractmethod


class Tech(ABC):

    @abstractmethod
    def activate():
        pass

    @abstractmethod
    def deactivate():
        pass
