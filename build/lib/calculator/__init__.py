""" This is the Calculator Class"""
from calculator.history import History
from calculator.calculator1 import Addition, Sub, Mutiply, Division


class Calculator:
    """ This is the default result property"""
    @staticmethod
    def add(values):
        """Addition of list"""
        additions = Addition(values)
        #a.validate_input()
        History.add_history(values, "Addition of", additions.get_output())
        return additions.get_output()

    @staticmethod
    def subtract(values):
        """Substraction encapsulated"""
        a = Sub(values)
        History.add_history(values, "Substraction of", a.get_output())
        return a.get_output()

    @staticmethod
    def multiply(values):
        a = Mutiply(values)
        History.add_history(values, "Multiplication of", a.get_output())
        return a.get_output()

    @staticmethod
    def divide(values):
        a = Division(values)
        History.add_history(values, "Division of", a.get_output())
        return a.get_output()

    @staticmethod
    def clear_history():
        History.clear_stored_history()
        return True

    @staticmethod
    def get_all_history():
        return History.stored_history

    @staticmethod
    def get_latest_calculation():
        return History.latest_calculation()

    @staticmethod
    def count_of_history():
        return History.count_history()

    @staticmethod
    def latest_calc_result():
        return History.get_latest_calc_result()

    @staticmethod
    def first_calc_result():
        return History.get_first_calc_result()
