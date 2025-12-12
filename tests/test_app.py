import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import *
import pytest

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

def test_sub_negative():
    assert sub(5, 22) == -17

# ------------------------------ #
# ---- multiplication tests ---- #
# ------------------------------ #
def test_mult():
	assert mult(5, 6) == 30

def test_mult_half():
	assert mult(0.5, 8) == 4

def test_mult_negative():
	assert mult(-5, 1) == -5

# ------------------------ #
# ---- division tests ---- #
# ------------------------ #
def test_div():
    assert div(10, 5) == 2 

def test_div_decimal():
    assert div(6, 1.5) == 4

def test_div_negative():
    assert div(10, -2) == -5

def test_div_zero():
    with pytest.raises(ZeroDivisionError) as error:
        div(5, 0)
    assert str(error.value) == "Division by zero"

# ------------------------- #
# ---- logarithm tests ---- #
# ------------------------- #
def test_log():
    assert log(100) == 2

def test_log_base2():
    assert log(8, 2) == 3

def test_log_1_base10():
    assert log(1) == 0

def test_log_1_diff_base():
    assert log(1, 52) == 0

def test_log_same_base():
    assert log(6, 6) == 1

def test_log_base0():
    with pytest.raises(ValueError) as error:
        log(5, 0)
    assert str(error.value) == "Value out of domain range"

def test_log_value0():
    with pytest.raises(ValueError) as error:
        log(0)
    assert str(error.value) == "Value out of domain range"

# ---------------------- #
# ---- square tests ---- #
# ---------------------- #
def test_square():
    assert square(5) == 25

def test_square_decimal():
    assert square(0.5) == 0.25

def test_square_negative():
    assert square(-4) == 16

def test_square_0():
    assert square(0) == 0

def test_square_1():
    assert square(1) == 1

# -------------------- #
# ---- sine tests ---- #
# -------------------- #
def test_sin_0():
    assert sin(0) == 0

def test_sin_pi_half():
    assert sin(math.pi/2) == 1

def test_sin_pi():
	assert sin(math.pi) == 0

# ---------------------- #
# ---- cosine tests ---- #
# ---------------------- #
def test_cos_0():
    assert cos(0) == 1

def test_cos_pi():
    assert cos(math.pi) == -1

def test_cos_pi_half():
    assert cos(math.pi/2) == 0

# --------------------- #
# ---- square root ---- #
# --------------------- #
def test_sq_root():
    assert sq_root(25) == 5

def test_sq_root_0():
    assert sq_root(0) == 0

def test_sq_root_1():
    assert sq_root(1) == 1

# -------------------- #
# ---- percentage ---- #
# -------------------- #
def test_percent_of100():
    assert percent(10, 100) == 10

def test_percent_ofself():
    assert percent(5, 5) == 100

def test_percent_0():
    assert percent(0, 300) == 0