class calculator:
    """
    Calculator class that is able
    to do calculations
    (dot product, addition, sub-
    traction) of 2 vectors.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates and prints dot product"""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds and prints result of two vectors"""
        result = list(float(x + y) for x, y in zip(V1, V2))
        print(f"Add Vector is: {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtracts and prints result of two vectors"""
        result = list(float(x - y) for x, y in zip(V1, V2))
        print(f"Sous Vector is: {result}")


"""
@staticmethod:

The @staticmethod decorator is used to define a static method
within a class. A static method is a method that is bound to
the class and not the instance. It can be called on the
class itself, without needing to create an instance of the class.
Use cases:
When a method doesn't depend on instance-specific
data and is primarily related to the class itself.
Utility functions that are relevant to the class
but don't need access to instance attributes.
"""

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# zipped_data = zip(names, scores)

# # Converting the zipped data to a list
# zipped_list = list(zipped_data)

# print(zipped_data)
