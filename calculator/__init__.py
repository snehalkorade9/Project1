""" This is the Calculator Class"""
from calculator.calculator1 import Addition, Sub, Mutiply, Division


class Calculator:
    """ This is the default result property"""
    @staticmethod
    def add(values):
        a = Addition(values)
        a.validate_input()
        return a.get_output()

    @staticmethod
    def subtract(values):
        a = Sub(values)
        return a.get_output()

    @staticmethod
    def multiply(values):
        a = Mutiply(values)
        return a.get_output()

    @staticmethod
    def divide(values):
        a = Division(values)
        return a.get_output()
