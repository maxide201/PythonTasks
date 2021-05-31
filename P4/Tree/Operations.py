class Operation:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def count(self):
        pass

    def stack(self):
        pass


class Add(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit) + int(self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        return self.num1.stack() + '\n' + self.num2.stack() + '\n' + 'ADD'

    def __str__(self) -> str:
        return f'({self.num1} + {self.num2})'


class Mul(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit) * int(self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        return self.num1.stack() + '\n' + self.num2.stack() + '\n' + 'MUL'

    def __str__(self) -> str:
        return f'({self.num1} * {self.num2})'


class Sub(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.digit = int(self.num1.digit) - int(self.num2.digit)

    def count(self):
        return self.digit

    def stack(self):
        return self.num1.stack() + '\n' + self.num2.stack() + '\n' + 'SUB'

    def __str__(self) -> str:
        return f'({self.num1} - {self.num2})'


class Num:
    def __init__(self, digit):
        self.digit = digit

    def stack(self):
        return 'PUSH ' + str(self.digit)

    def __str__(self) -> str:
        return str(self.digit)
