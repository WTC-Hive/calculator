import math

def add(a, b):
    """
    Add two numbers and return the result.
    """
    return sum([a, b])

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    """
    return sum([a, -b])

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    return a * b

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    Handle division by zero by returning "Error: Division by zero".
    """
    return a / b if b != 0 else "Error: Division by zero"

def sqrt(a):
    """
    Return the square root of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    return math.sqrt(a) if a >= 0 else "Error: Negative input"

def modulus(a, b):
    """
    Return the remainder of the division of the first number by the second.
    Handle division by zero by returning "Error: Division by zero".
    """
    return a % b if b != 0 else "Error: Division by zero"

def exponent(a, b):
    """
    Return the result of raising the first number to the power of the second.
    """
    return a ** b
