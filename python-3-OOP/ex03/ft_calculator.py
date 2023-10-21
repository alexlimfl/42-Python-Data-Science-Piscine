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
