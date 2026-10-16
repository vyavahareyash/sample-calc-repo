from math_lib.calculator import calculate_fibonacci
import pytest

def test_fibonacci_base():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1

def test_fibonacci_sequence():
    assert calculate_fibonacci(2) == 1
    assert calculate_fibonacci(3) == 2
    assert calculate_fibonacci(4) == 3
    assert calculate_fibonacci(5) == 5

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        calculate_fibonacci(-1)
