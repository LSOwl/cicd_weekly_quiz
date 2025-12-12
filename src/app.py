import math

def add (a, b):
    return a+b

def sub (a, b):
    return a-b

def mult (a, b):
    return a*b

def div (a, b):
    return a/b

def log (a, base=10):
    return math.log(a, base)

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
    return a**0.5