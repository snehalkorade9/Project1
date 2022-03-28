"""This function computes the calculation history"""
class History:
    """This class gives the """
    stored_history = []


    def __new__(cls):
        """ This is a singleton method.
        Singleton  creates an instance only if there is no instance created so far;
         otherwise, it will return the instance that is already created."""
        if not hasattr(cls, 'instance'):
            cls.instance = super(History, cls).__new__(cls)
        return cls.instance

    @classmethod
    def clear_stored_history(cls):
        """Clear all history"""
        cls.stored_history.clear()
        return True

    @classmethod
    def add_history(cls, value, operation, result):
        """Operation added to history"""
        cls.stored_history.append({"Numbers": [value], "Operation": operation, "Output": result})
        return cls.count_history()

    @classmethod
    def count_history(cls):
        """gives count of total operation performed"""
        return len(cls.stored_history)

    @classmethod
    def latest_calculation(cls):
        """gives last operation performed"""
        return History.stored_history[-1]

    @classmethod
    def get_latest_calc_result(cls):
        """gives result of last operation performed"""
        return History.stored_history[-1]['Output']

    @classmethod
    def get_first_calc_result(cls):
        """gives result of first operation performed"""
        return History.stored_history[0]['Output']
