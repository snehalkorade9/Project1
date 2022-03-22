"""This test the homepage"""
from _pytest.fixtures import fixture

from calculator1.Operations import Addition, Substraction, Multiply, Divide


@fixture
def create_data() -> tuple[float, float, float]:
    return 6.0, 2.0, 2.0


def test_addition(create_data):
    """This makes the index page"""
    a = Addition()
    assert a.get_result(create_data) == 10


def test_substraction(create_data):
    """This makes the index page"""
    a = Substraction()
    assert a.get_result(create_data) == 2


def test_multiply(create_data):
    """This makes the index page"""
    a = Multiply()
    assert a.get_result(create_data) == 24


def test_divide(create_data):
    """This makes the index page"""
    a = Divide()
    assert a.get_result(4.0, 2.0) == 2


def test_divide_zero():
    a = Divide()
    assert(a.get_result(5, 0), ZeroDivisionError)
