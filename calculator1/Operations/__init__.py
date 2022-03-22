
"""All the calaculator functions"""


class Addition:
    """Addition function"""
    result = 0

    def get_result(self, num: tuple[float, float, float]):
        """Add numbers"""
        print(num)
        for i in num:
            self.result = self.result+i
        return self.result


class Substraction:
    """Substraction class"""
    result = 0

    def get_result(self, num: tuple[float, float, float]):
        """Multiply numbers"""
        for i in num:
            self.result = i - self.result
        return self.result


class Multiply:
    """Multiply class"""
    result = 1

    def get_result(self, num: tuple[float, float, float]):
        """Multiply numbers"""
        for i in num:
            self.result = i*self.result
        return self.result


class Divide:
    """Divide class"""

    def get_result(self, value_1, value_2):
        """divide numbers"""
        try:
            result = value_1/value_2

        except ZeroDivisionError as e:
            raise e

        return result
