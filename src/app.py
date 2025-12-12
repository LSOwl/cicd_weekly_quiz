import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")

def log (a, base=10):
    try:
        return math.log(a, base)
    except ValueError:
        raise ValueError("Value out of domain range")

def square (a):
    return a**2

def sin (a):
    # truncate result to 2 decimal places (avoids roundoff error with
    # python implementation of pi in math.pi)
    result = float(f"{math.sin(a):.2f}")
    return result

def cos (a):
    result = float(f"{math.cos(a):.2f}")
    return result

def sq_root(a):
    if a < 0:
        raise ValueError("Value cannot be negative")
    else:
        return a**0.5

def percent(a, b):
    decimal = a/b
    return decimal * 100