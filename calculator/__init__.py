import Operations
""" This is the Calculator Class"""


class Calculator:
    """ This is the default result property"""
    result = 0

    @staticmethod
    def create():
        return 2, 4, 5

    def add(self):
        """ This is the add method"""
        add1 = Operations.Addition()
        add1.add()

    def subtract(self, value_1):
        """ This is the subtract method"""
        self.result = self.result - value_1
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
