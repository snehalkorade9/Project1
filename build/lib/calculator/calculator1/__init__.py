from calculator.operation import Operation


class Calculations:
    """This is the base class
    The below method is a constructor which will set the data to be used for calculation
    The get_output method is overridden by all the below
    classes to return the output and the output differs from operation to operation"""
    def __init__(self, list_passed_by_user):
        self.list_1 = list_passed_by_user

    # def validate_input(self):
    #     if type(self.list_1) != int:
    #         raise ValueError("Minimum 2 values expected")

    def get_output(self):
        print("Output")


class Addition(Calculations):
    """The get_output method in calculator class calls the addition method in operations
     class where the actual addition is performed, here the user cannot directlly access the basic
     implementation of the function rather it has to call the get_output method to do the same
     Here Abstraction is also achieved as """

    def get_output(self):
        result = 0
        for i in self.list_1:
            result = Operation.add(i, result)
        return result


class Sub(Calculations):
    """Here the get_output method is getting substraction result"""

    def get_output(self):
        result = self.list_1[0]
        print("List:", self.list_1)
        for i in range(1, len(self.list_1)):
            result = Operation.sub(result, self.list_1[i])
        return result


class Mutiply(Calculations):
    """This class multiplies the input"""

    def get_output(self):
        result = 1
        for i in self.list_1:
            result = Operation.multi(i, result)
        return result


class Division(Calculations):
    """In this class we encapsulate the original Division function so that it cannot be
    accessed directly rather it should be accessed through get_output method"""
    def get_output(self):
        if len(self.list_1) > 2:
            raise Exception("Invalid input")
        numerator = self.list_1[0]
        denomator = self.list_1[1]
        try:
            result = Operation.div(numerator, denomator)

        except ZeroDivisionError:
            raise ZeroDivisionError("Divide by 0 not allowed")

        return result
