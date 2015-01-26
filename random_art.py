import random
from math import pi, sin, cos

"""Your job is to create better version of create_expression and
run_expression to create random art.
Your expression should have a __str__() function defined for it."""

class Expression:
    def __init__(self):
        self.commands = []

    def evaluate(self, x, y):
        value = 1
        for (command, coord) in self.commands:
            if command == "one" and coord == "x":
                value = cos(pi * sin(pow(x, 2)))
            elif command == "one" and coord == "y":
                value = sin(pi * cos(pow(y, 4)))
            elif command == "two" and coord == "x":
                value *= pow(cos(pi * x), 2)
            elif command == "two" and coord == "y":
                value *= cos(pi * y)
            elif command == "three" and coord == "x":
                value *= sin(pi * sin(pi * x))
            elif command == "three" and coord == "y":
                value *= sin(pi * sin(pi * y))

        return value

    def __str__(self):
        return str(self.commands)

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    #expr = lambda x, y: sin(x)
    #return expr

    expr = Expression()
    for _ in range(12):
        if random.random() > 0.5:
            x_or_y = "x"
        else:
            x_or_y = "y"

        if random.random() > 0.7:
            operator = "one"
        elif random.random() < 0.3:
            operator = "two"
        else:
            operator = "three"

        expr.commands.append([operator, x_or_y])

    return expr



def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr.evaluate(x, y)
