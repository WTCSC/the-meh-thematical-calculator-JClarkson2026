import pytest
from mathcalc import add, subtract, multiply, divide

def test_addPositive():
    """Test addition of two positive numbers."""
    assert add(3, 5) == 8

def test_addNegative():
    """Test addition of two negative numbers."""
    assert add(-3, -5) == -8

def test_subPositive():
    """Test subtraction of two positive numbers."""
    assert subtract(8, 5) == 3

def test_subNegative():
    """Test subtraction of two negative numbers."""
    assert subtract(3, 5) == -2

def test_multiplyPositive():
    """Test multiplication of two positive numbers."""
    assert multiply(4, 5) == 20

def test_multiplyZero():
    """Test multiplication by zero."""
    assert multiply(4, 0) == 0

def test_dividePositive():
    """Test division of two positive numbers."""
    assert divide(20, 5) == 4

def test_divideByZero():
    """Test division by zero."""
    assert divide(5, 0) == "wow... you're such an incredibley smart person, I bet your dad is proud of you"

def test_divideByOne():
    """Test division by one."""
    assert divide(5, 1) == 5