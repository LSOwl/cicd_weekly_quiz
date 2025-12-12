import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import *

def test_add():
    assert add(5, 6) == 11
    assert add(5, 6) != 10

def test_sub():
    assert sub(10, 4) == 6
    assert sub(5, 22) == -17

def test_mult():
	assert mult(5, 6) == 30
	assert mult(0.5, 8) == 4
	assert mult(-5, 1) == -5

def test_div():
    assert div(10, 5) == 2
    assert div(6, 1.5) == 4
    assert div(10, -2) == -5

def test_log():
    assert log(100) == 2
    assert log(8, 2) == 3