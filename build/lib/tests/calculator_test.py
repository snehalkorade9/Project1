"""This test the homepage"""
import pytest
from _pytest.fixtures import fixture

from calculator import Calculator


@fixture
def create_data():
    return 10.0, 2, 2

def test_addition(create_data):
    """This makes the index page"""
    assert (Calculator.add(create_data)) == 14

#
# def test_substraction(create_data):
#     """This makes the index page"""
#     assert (Calculator.subtract(create_data)) == 6
#
#
# def test_multiply(create_data):
#     """This makes the index page"""
#     assert (Calculator.multiply(create_data)) == 40
#
#
# def test_divide(create_data):
#     """This makes the index page"""
#     assert (Calculator.divide((10,2))) == 5
#
#
# def test_divide_zero():
#     with pytest.raises(ZeroDivisionError, match="Divide by 0 not allowed"):
#         Calculator.divide((5, 0))
#
# # def test_invalid_exception():
# #     with pytest.raises(ZeroDivisionError, match="Invalid input"):
# #         Calculator.divide(create_data)
#
