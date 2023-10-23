def callLimit(limit: int):
    """
    Decorator function that takes in an
    integer argument limit,
    which specifies the number of times
    a decorated function can call.
    """
    count = 0
    def callLimiter(function):
        """A nested function"""
        def limit_function(*args: any, **kwds: any):
            """
            A wrapper function that wraps around the original function
            (function). It tracks the number of times the wrapped function
            has been called using a count variable.
            """
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function
    return callLimiter

"""
# @callLimit(3) is just an easier way of saying f = callLimit(3)
@callLimit(3) #pie-syntax
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
    f()
    g()
"""