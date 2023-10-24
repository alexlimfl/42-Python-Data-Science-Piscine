from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """Descriptive string representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """More detailed and developer-oriented representation"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """Descriptive string representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """More detailed and developer-oriented representation"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        This is a class method, which is a method bound
        to the class rather than an instance
        used to create new Lannister objects
        """
        object = cls(first_name)
        object.is_alive = is_alive
        return object


"""
@classmethod:

The @classmethod decorator is used to define a class method within a class.
A class method is bound to the class and takes the class itself as its
first argument (typically named cls). Class methods can be called on
the class itself, and they can access and modify class-level attributes.
Use cases:
When a method operates on class-level data and requires access to
the class itself.
Factory methods that create instances of the class with specific
characteristics.
"""
