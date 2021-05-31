class CalcVisitor:
    def visit(self, expression):
        return expression.count()


class PrintVisitor:
    def visit(self, expression):
        return expression


class StackVisitor:
    __stack = ''

    def visit(self, expression):
        self.__stack = expression.stack()

    def get_code(self):
        return self.__stack
