import pytest

import myapp.mymodule.funcs as F


@pytest.mark.easy_operation
def test_add():
    # This test will fail.
    assert F.add(4, 8) == 12

@pytest.mark.easy_operation
def test_subtract():
    assert F.subtract(3, 6) == -3

@pytest.mark.difficult_operation
def test_multiply():
    assert F.multiply(4, 5) == 20

@pytest.mark.difficult_operation
def test_divide():
    assert F.divide(56, 8) == 7
