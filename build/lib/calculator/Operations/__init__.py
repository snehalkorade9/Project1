
"""All the calaculator functions"""


class Operation:
    """Addition function
    The below method is defined static as we are not changing the state of class"""

    @classmethod
    def add(cls, value1, value2):
        """Add numbers"""
        result = value1+value2
        return result

    @classmethod
    def sub(cls, value1, value2):
        """Substract numbers"""
        result = value1 - value2
        return result

    @classmethod
    def multi(cls, value1, value2):
        """Multiply numbers"""
        result = value1 * value2
        return result

    @classmethod
    def div(cls, value1, value2) -> float:
        """Divide numbers"""
        result = value1/value2
        return result
