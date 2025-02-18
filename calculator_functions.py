def add(a, b):
    """
    Add two numbers and return the result.
    """
    result = a + b
    return f"{a} + {b} = {result}"

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    """
    result = a - b
    return f"{a} - {b} = {result}"

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    result = a * b
    return f"{a} * {b} = {result}"

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    Handle division by zero by returning "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    else:
        result = a / b
        return f"{a} / {b} = {result}"

def sqrt(a):
    """
    Return the square root of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    if a < 0:
        return "Error: Negative Input"
    else:
        result = a ** 0.5
        return f"{a} ** 2 = {result}"

def modulus(a, b):
    """
    Return the remainder of the division of the first number by the second.
    Handle division by zero by returning "Error: Division by zero".
    """
    if b == 0:
        return "Error: Division by zero"
    else:
        result = a % b
        return f"{a} % {b} = {result}"

def exponent(a, b):
    """
    Return the result of raising the first number to the power of the second.
    """
    result = a ** b
    return f"{a} ** {b} = {result}"
