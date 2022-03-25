
"""All the calaculator functions"""

class Addition:
    """Addition function"""
    @classmethod
    def add(cls, value1, value2,):
        """Add numbers"""
        result = value1+value2
        return result


class Substraction:
    """Substraction class"""
    @classmethod
    def sub(cls, value1, value2, ):
        """Add numbers"""
        result = value1 - value2
        return result


class Multiplication:
    """Multiply class"""

    @classmethod
    def mult(cls, value1, value2, ):
        """Add numbers"""
        result = value1 * value2
        return result


class Divide:
    """Divide class"""

    @classmethod
    def div(cls, value1, value2, ) -> float:
        """Add numbers"""
        result = value1/value2
        return result
