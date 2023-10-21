class calculator:
    """Calculator class for vector with a scalar"""
    def __init__(self, vector):
        """Method of contructor for vector list provided"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addtion magic method"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)
    
    def __mul__(self, object) -> None:
        """Multiplication magic method"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)
    
    def __sub__(self, object) -> None:
        """Subtraction magic method"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division magic method"""
        try:
            if object == 0:
                raise ZeroDivisionError("Division by 0 isn't allowed!")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print("Error:", e)



# v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v1 + 5
# print("---")
# v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v2 * 5
# print("---")
# v3 = calculator([10.0, 15.0, 20.0])
# v3 - 5
# v3 / 5




"""
$> python tester.py
[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
---
[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]
---
[5.0, 10.0, 15.0]
[1.0, 2.0, 3.0]
$>
"""