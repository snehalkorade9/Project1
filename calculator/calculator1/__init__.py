"""All Calculation functions"""

from abc import abstractmethod
from calculator.operation import Operations


class Calculations:
    """This is the base class
    The base class here is not dependend on any of the derived class rather depends on abstraction
    The below method is a constructor which will set the data to be used for calculation
     The get_output method is overridden by all the below
    classes to return the output and the output differs from operation to operation"""
    def __init__(self, list_passed_by_user):
        self.list_1 = list_passed_by_user

    @abstractmethod
    def get_output(self):
        """This method is defined obeys the O - Open-closed Principle and
        L - Liskov Substitution Principle of SOLID.
        The method getout does the same function on all the class
         of getting output but the output differs
        on the operation, this method is therefore overriden by all the functions
        The L - Liskov Substitution Principle states that the derived class should be used
         in substitution of base
        class, here we can use all the methods of the base class without changing the basic
         implementation in derived
        class without any unexpected behavior change to the base class.
        The Dependency Inversion principle states that our classes should depend upon interfaces or
        abstract classes instead of concrete classes and functions. Here there is just
        one dependency that is also
        set on abstract class that is get_output as each calculation will have a output"""
        pass

        def error_failed():
            pass

class Addition(Calculations):
    """The get_output method in calculator class calls the addition method in operations
     class where the actual addition is performed, here the user cannot directlly access the basic
     implementation of the function rather it has to call the get_output method to do the same
     Here Abstraction is also achieved as the by encapsulation of data"""

    def get_output(self):
        result = 0
        for i in self.list_1:
            result = Operations.add(i, result)
        return result


class Sub(Calculations):
    """Here the get_output method is getting substraction result"""

    def get_output(self):
        result = self.list_1[0]
        print("List:", self.list_1)
        for i in range(1, len(self.list_1)):
            result = Operations.sub(result, self.list_1[i])
        return result


class Mutiply(Calculations):
    """This """

    def get_output(self):
        result = 1
        for i in self.list_1:
            result = Operations.multi(i, result)
        return result


class Division(Calculations):
    """In this class we encapsulate the original Division function so that it cannot be
    accessed directly rather it should be accessed through get_output method"""
    def get_output(self):
        # if len(self.list_1) > 2:
        #     raise Exception("Invalid input")
        numerator = self.list_1[0]
        denomator = self.list_1[1]
        try:
            result = Operations.div(numerator, denomator)

        except ZeroDivisionError:
            raise ZeroDivisionError("Divide by 0 not allowed")

        return result
