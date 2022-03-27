"""This test the homepage"""
import pytest
from _pytest.fixtures import fixture
from calculator import Calculator
from calculator.History import History

@fixture
def clear_hist():
    History.clear_history()


@fixture
def set_data():
    value= 2, 4, 5
    a = Calculator.multiply((2,4))
    History.add_history(a)

def test_clear_history(clear_hist, set_data):
    """This makes the index page"""
    History.count_history() == 1
    print("History:", History.history)
    History.clear_history()
    History.count_history() == 0
    assert History.clear_history()==True
