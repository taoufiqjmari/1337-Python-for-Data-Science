def square(x: int | float) -> int | float:
    """Count square of a number"""
    return x * x


def pow(x: int | float) -> int | float:
    """Count power of a number"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    A wrapper around a function that doesn't
    initiate initial value each time called
    """
    def inner() -> float:
        """
        The modif on the function
        """
        nonlocal x
        result = function(x)
        x = result
        return result
    return inner
