import pytest
from calc import divide, average


def test_divide():
    assert divide(6, 3) == 2


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_average():
    assert average([2, 4, 6]) == 4
