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


def test_substraction(create_data):
    """This makes the index page"""
    assert (Calculator.subtract(create_data)) == 6


def test_multiply(create_data):
    """This makes the index page"""
    assert (Calculator.multiply(create_data)) == 40


def test_divide(create_data):
    """This makes the index page"""
    assert (Calculator.divide((10,2))) == 5


def test_divide_zero():
    with pytest.raises(ZeroDivisionError, match="Divide by 0 not allowed"):
        Calculator.divide((5, 0))

# def test_invalid_exception():
#     with pytest.raises(ZeroDivisionError, match="Invalid input"):
#         Calculator.divide(create_data)


@fixture
def clear_hist():
    Calculator.clear_history()


@fixture
def set_data():
    value = 10, 4
    Calculator.add(value)
    Calculator.multiply(value)
    Calculator.divide(value)
    Calculator.subtract(value)


def test_clear_history(clear_hist, set_data):
    """This makes the index page"""
    Calculator.get_all_history()
    Calculator.clear_history()
    assert (Calculator.count_of_history() == 0)
    # assert (Calculator.clear_history() == True)


def test_total_history(clear_hist, set_data):
    assert (Calculator.count_of_history() == 4)


def test_latest_calc(clear_hist, set_data):
    assert (Calculator.get_latest_calculation() == {'Numbers': [(10, 4)], 'Operation': 'Substraction of',
                                                    'Output': 6})


def test_get_latest_result(clear_hist, set_data):
    assert (Calculator.latest_calc_result() == 6)


def test_get_first_result(clear_hist, set_data):
    assert (Calculator.first_calc_result() == 14)

def test_data_adding_history():
    Calculator.clear_history()
    assert (Calculator.count_of_history() == 0)
    Calculator.add((2,4))
    assert (Calculator.count_of_history() == 1)
    assert (Calculator.get_latest_calculation() == {'Numbers': [(2, 4)], 'Operation': 'Addition of',
                                                    'Output': 6})


