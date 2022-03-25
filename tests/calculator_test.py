"""This test the homepage"""
from _pytest.fixtures import fixture
from calculator1 import Calculations, Addition, Sub, Mutiply, Division


@fixture
def create_data():
    return 10, 6, 2

def test_addition(create_data,create_object):
    """This makes the index page"""
    a= Addition(create_data)
    assert a.get_output(Addition) == 18


def test_substraction(create_data):
    """This makes the index page"""
    a = Calculations(create_data)
    assert Sub.get_output(Sub) == 2


def test_multiply(create_data):
    """This makes the index page"""
    a = Calculations(create_data)
    assert Mutiply.get_output() == 120


def test_divide(create_data):
    """This makes the index page"""
    a = Calculations(create_data)
    assert Division.get_output(list[5, 0]) == 120


def test_divide_zero():
    assert(Division.get_output(list[5, 0]), ZeroDivisionError)
