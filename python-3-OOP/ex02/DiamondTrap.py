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


# Joffrey = King("Joffrey")
# print(Joffrey.__dict__)
# Joffrey.set_eyes("blue")
# Joffrey.set_hairs("light")
# print(Joffrey.get_eyes())
# print(Joffrey.get_hairs())
# print(Joffrey.__dict__)

"""
$> python tester.py
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hair': 'dark'}
blue
light
{'first_name': 'Joffrey', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'blue', 'hairs': 'light'}
$>
8
"""