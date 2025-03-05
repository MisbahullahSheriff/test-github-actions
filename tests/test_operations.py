from src.math_operations import addition, subtraction


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0


def assert_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(-3, 3) == -6
    assert subtraction(3, -3) == 2 