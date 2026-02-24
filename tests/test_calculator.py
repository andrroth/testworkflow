"""Tests for the calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide, power, factorial


class TestCalculator:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(-2, 3) == -6
        assert multiply(0, 100) == 0

    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_power(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(2, -1) == 0.5

    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120

    def test_factorial_negative(self):
        with pytest.raises(ValueError, match="not defined for negative"):
            factorial(-1)
