
"""All the calaculator functions"""


class Addition:
    """Addition function"""
    result = 0

    def get_result(self, num: tuple[int, int, int]):
        """Add numbers"""
        print(num)
        for i in num:
            self.result = self.result+i
        return self.result


class Substraction:
    """Substraction class"""
    result = 0

    def get_result(self, num: tuple[int, int, int]):
        """Multiply numbers"""
        for i in num:
            self.result = i - self.result
        return self.result


class Multiply:
    """Multiply class"""
    result = 1

    def get_result(self, num: tuple[int, int, int]):
        """Multiply numbers"""
        for i in num:
            self.result = i*self.result
        return self.result


class Divide:
    """Divide class"""

    def get_result(self, num: tuple[int, int, int]):
        """Multiply numbers"""
            result = num[0]/num[1]
            return result

