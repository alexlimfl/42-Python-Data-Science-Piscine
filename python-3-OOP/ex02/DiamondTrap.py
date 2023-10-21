from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King."""
    def __init__(self, first_name, is_alive=True):
        """
        Method to the construct/initialise class instance.
        super() constructs superclasses based on MRO.
        If family is Baratheon, means it constructs Lannister first.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Method to set eyes color"""
        self.eyes = color

    def set_hairs(self, color):
        """Method to set hair color"""
        self.hairs = color

    def get_eyes(self):
        """Method to return eyes color object"""
        return self.eyes

    def get_hairs(self):
        """Method to return hair color object"""
        return self.hairs
