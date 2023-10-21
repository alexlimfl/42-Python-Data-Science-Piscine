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


class Stark(Character):
    """Representing the Stark family."""
    def __init__(self, first_name, is_alive=True):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
