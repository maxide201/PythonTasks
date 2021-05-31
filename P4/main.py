from MyDictFiles.MyDict import MyDict
from Tree.Operations import Mul, Add, Num
from Tree.Visitors import PrintVisitor, CalcVisitor, StackVisitor
from Html import Html


# Задание со словарем
def task1():
    dictionary = MyDict()

    # заполнение словаря
    for i in range(5000):
        dictionary[i] = i
        assert dictionary[i] == i

    # поддержка len
    assert len(dictionary) == 5000

    # поддержка for
    for key, value in dictionary:
        pass


class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


# Задание с вызовом встроеннйо функции
def task2():
    myclass = MyClass('qwer', 1234, 20.00001)
    print(vars(myclass))


# работа с деревом выражений
def task3():
    ast = Add(Num(7), Mul(Num(3), Num(2)))
    pv = PrintVisitor()
    cv = CalcVisitor()
    sv = StackVisitor()
    print(pv.visit(ast))
    print(cv.visit(ast))
    sv.visit(ast)
    print(sv.get_code())


# заданеи с html-тегами
def task4():
    html = Html.Html()

    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')

    print(html.data)


# Запуск тестов
task1()
task2()
task3()
task4()