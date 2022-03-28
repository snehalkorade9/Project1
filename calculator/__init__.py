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
        hist = History()
        hist.add_history(values, "Addition of", additions.get_output())
        return additions.get_output()

    @staticmethod
    def subtract(values):
        """Substraction encapsulated"""
        substraction = Sub(values)
        hist = History()
        hist.add_history(values, "Substraction of", substraction.get_output())
        return substraction.get_output()

    @staticmethod
    def multiply(values):
        """Mutliply"""
        multiplication = Mutiply(values)
        hist = History()
        hist.add_history(values, "Multiplication of", multiplication.get_output())
        return multiplication.get_output()

    @staticmethod
    def divide(values):
        """Divide"""
        division = Division(values)
        hist = History()
        hist.add_history(values, "Division of", division.get_output())
        return division.get_output()

    @staticmethod
    def clear_history():
        """clear calculation"""
        hist = History()
        hist.clear_stored_history()
        return True

    @staticmethod
    def get_all_history():
        """Get all calculation"""
        hist = History()
        return hist.stored_history

    @staticmethod
    def get_latest_calculation():
        """Get latest calculation"""
        hist = History()
        return hist.latest_calculation()

    @staticmethod
    def count_of_history():
        """Get count of history"""
        hist = History()
        return hist.count_history()

    @staticmethod
    def latest_calc_result():
        """Get last calculation result"""
        hist = History()
        return hist.get_latest_calc_result()

    @staticmethod
    def first_calc_result():
        """Get first calculation result"""
        hist = History()
        return hist.get_first_calc_result()
