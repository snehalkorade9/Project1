from calculator1.Operations import Addition


class Calculator:
    def create_list(self) -> tuple[float, float, float]:
        return 2.0, 4.0, 6.0

    def Add(self):
        add = Addition()
        a = Addition()
        print(a.get_result(self.create_list))

