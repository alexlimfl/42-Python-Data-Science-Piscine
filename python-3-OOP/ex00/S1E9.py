from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class (Parent)"""
    @abstractmethod
    def __init__(self, first_name, is_alive = True):
        """Your docstring for Constructor"""
        self.first_name = "DigBick"
        self.is_alive = is_alive
        pass

class Stark(Character): 
    """Your docstring for Class"""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
    def die(self, is_alive=False):
        """Your docstring for Method"""
        self.is_alive = is_alive




Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)

"""expected output:
$> python tester.py
{'first_name': 'Ned', 'is_alive': True}
True
False
Your docstring for Class
Your docstring for Constructor
Your docstring for Method
---
{'first_name': 'Lyanna', 'is_alive': False}
$>
"""
