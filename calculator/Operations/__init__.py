
"""All the calaculator functions"""


class Operation:
    """Addition function"""
    """The below method is defined static as we are not changing the state of class"""
    def add(value1, value2):
        """Add numbers"""
        result = value1+value2
        return result

    def sub(value1, value2):
        """Add numbers"""
        result = value1 - value2
        return result

    def multi(value1, value2):
        """Add numbers"""
        result = value1 * value2
        return result

    def div(value1, value2) -> float:
        """Add numbers"""
        result = value1/value2
        return result
