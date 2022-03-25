from calculator1.Operations import Addition as Alias_add, Substraction, Multiplication, Divide


class Calculations:
    """This is the base class"""
    def __init__(self, list_passed_by_user):
        self.list_1 = list_passed_by_user


class Addition(Calculations):
    """The get_output method in calculator class calls the addition method in operations class where the actual addition is performed, here the user cannot directlly access the basic implementation of the function rather it has to call the get_output method to do the same"""
    def get_output(self):
        result = 0
        for i in self.list_1:
            result = Addition.add(i, result)
        return result


class Sub(Calculations):
    """Here the get_output method is getting substraction result"""
    def get_output(self):
        result = 0
        for i in self.list_1:
            result = Substraction.sub(i, result)
        return result


class Mutiply(Calculations):
    def get_output(self):
        result = 1
        for i in self.list_1:
            result = Multiplication.mult(i, result)
        return result


class Division(Calculations):
    def get_output(self):
        result = 1
        for i in self.list_1:
            result = Divide.div(i, result)
        return result
