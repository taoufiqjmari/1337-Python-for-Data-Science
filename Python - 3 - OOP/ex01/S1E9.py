from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of base class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method in Character class"""
        pass


class Stark(Character):
    """Direved class from Character class"""
    def __init__(self, first_name, is_alive=True):
        """Constructor of derived class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Implementation of abstract method"""
        self.is_alive = False
