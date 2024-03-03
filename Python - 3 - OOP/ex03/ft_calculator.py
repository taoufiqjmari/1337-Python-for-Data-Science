class calculator:
    """A calculator of a vector with a scalar"""
    def __init__(self, vector):
        """Constructor"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Addition"""
        self.vector = [val + object for val in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication"""
        self.vector = [val * object for val in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substraction"""
        self.vector = [val - object for val in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division"""
        if object == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        self.vector = [val // object for val in self.vector]
        print(self.vector)
