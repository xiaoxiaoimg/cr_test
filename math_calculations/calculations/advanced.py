from .basic import subtract


class Calculator:
    def __init__(self):
        pass

    def divide(self, x, y):
        """Divide two numbers, with error checking."""
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

    def Calculatesquareroot(self, x):
        if x < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        print("Calculating square root of", x)
        return x**0.5
