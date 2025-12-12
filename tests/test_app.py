import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import *
from decimal import Decimal

# ------------------------ #
# ---- addition tests ---- #
# ------------------------ #
def test_add():
    assert add(5, 6) == 11

def test_add1():
    assert add(5, 6) != 10

# --------------------------- #
# ---- subtraction tests ---- #
# --------------------------- #
def test_sub():
    assert sub(10, 4) == 6

def test_sub1():
    assert sub(5, 22) == -17

# ------------------------------ #
# ---- multiplication tests ---- #
# ------------------------------ #
def test_mult():
	assert mult(5, 6) == 30

def test_mult1():
	assert mult(0.5, 8) == 4

def test_mult2():
	assert mult(-5, 1) == -5

# ------------------------ #
# ---- division tests ---- #
# ------------------------ #
def test_div():
    assert div(10, 5) == 2 

def test_div1():
    assert div(6, 1.5) == 4

def test_div2():
    assert div(10, -2) == -5

# ------------------------- #
# ---- logarithm tests ---- #
# ------------------------- #
def test_log():
    assert log(100) == 2

def test_log1():
    assert log(8, 2) == 3

def test_log2():
    assert log(1) == 0

def test_log3():
    assert log(1, 52) == 0

def test_log4():
    assert log(6, 6) == 1

# ---------------------- #
# ---- square tests ---- #
# ---------------------- #
def test_square():
    assert square(5) == 25

def test_square1():
    assert square(0.5) == 0.25

def test_square2():
    assert square(-4) == 16

def test_square3():
    assert square(0) == 0

def test_square4():
    assert square(1) == 1

# -------------------- #
# ---- sine tests ---- #
# -------------------- #
def test_sin():
    assert sin(0) == 0

def test_sin1():
    angle = math.pi/2
    assert sin(angle) == 1

# ---------------------- #
# ---- cosine tests ---- #
# ---------------------- #
def test_cos():
    assert cos(0) == 1

def test_cos1():
    assert cos(math.pi) == -1

def test_cos2():
    assert cos(math.pi/2) == 0