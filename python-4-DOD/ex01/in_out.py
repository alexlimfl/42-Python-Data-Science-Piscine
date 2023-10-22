def square(x: int | float) -> int | float:
    """Returns square of x"""
    return x ** 2

def pow(x: int | float) -> int | float:
    """Returns x power of x"""
    return x ** x

def outer(x: int | float, function) -> object:
    """outter function"""
    count = 0
    def inner() -> float:
        """inner function"""
        nonlocal count
        count += 1
        c = count
        result = x
        while c > 0:
            result = function(result)
            c -= 1
        return result
    return inner
