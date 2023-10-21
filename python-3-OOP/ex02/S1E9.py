from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class (Parent)"""
    @abstractmethod
    def __init__(self, first_name, is_alive):
        """Method to the construct/initialise class instance"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Method to kill"""
        self.is_alive = False

    def __str__(self) -> str:
        """Descriptive string representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """More detailed and developer-oriented representation"""
        return self.__str__()


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
