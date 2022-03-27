class History:
    history= []

    def clear_history():
        History.history.clear()
        return True

    def add_history(str):
        History.history.append(str)

    def count_history():
        return len(History.history)

    def latest_calculation(self):
        return History.history[-1]

