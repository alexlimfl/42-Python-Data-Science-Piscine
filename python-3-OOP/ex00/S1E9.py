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


"""
@abstractmethod:

The @abstractmethod decorator is part of Python's abstract base class (ABC)
module (abc) and is used to define abstract methods within an abstract class.
An abstract method is a method that has no implementation in the abstract class
and must be implemented by concrete subclasses. Abstract classes cannot be
instantiated.
Use cases:
When you want to define a common interface or contract for multiple classes,
requiring them to implement certain methods.
Ensuring that specific methods are implemented in subclasses.
"""
