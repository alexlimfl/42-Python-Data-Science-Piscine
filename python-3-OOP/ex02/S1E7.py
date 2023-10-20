from S1E9 import Character

class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True, ):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"
        # print("A")

class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True, ):
        """Method to the construct/initialise class instance"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"
        # print("B")

    @classmethod
    def create_lannister(cls,first_name, is_alive=True):
        """
        This is a class method, which is a method bound
        to the class rather than an instance
        used to create new Lannister objects

        """
        object = cls(first_name)
        object.is_alive = is_alive
        return object

# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# Jaine = Lannister.create_lannister("Jaine", True)
# print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")

"""
$> python tester.py
{'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'}
<bound method Baratheon.__str__ of Vector: ('Baratheon', 'brown', 'dark')>
<bound method Baratheon.__repr__ of Vector: ('Baratheon', 'brown', 'dark')>
True
False
Representing the Baratheon family.
---
{'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'}
<bound method Lannister.__str__ of Vector: ('Lannister', 'blue', 'light')>
True
---
Name : ('Jaine', 'Lannister'), Alive : True
$>"""