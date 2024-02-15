class calculator:
    """A calculator of a vector with a scalar"""
    def __init__(self, vector):
        """Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition"""
        result = [val + object for val in self.vector]
        print(result)

    def __mul__(self, object) -> None:
        """Multiplication"""
        result = [val * object for val in self.vector]
        print(result)

    def __sub__(self, object) -> None:
        """Substraction"""
        result = [val - object for val in self.vector]
        print(result)

    def __truediv__(self, object) -> None:
        """Division"""
        if object == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        result = [val // object for val in self.vector]
        print(result)
