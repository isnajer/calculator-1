"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    sum = num1 + num2
    return sum


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    diff = num1 - num2
    return diff

def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    prod = num1 * num2
    return prod

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    quo = num1/num2
    return quo

def square(num1):
    """Return the square of num1."""
    square = num1**2
    return square

def cube(num1):
    """Return the cube of num1."""
    cube = num1**3
    return cube

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power = num1**num2
    return power

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    mod = num1 % num2
    return mod
