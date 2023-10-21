from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True, ):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, ):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

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
