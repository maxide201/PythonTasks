# ВАРИАНТ 24
import math


def foo1(x, y):
    return (x ** 3 - 62 * x ** 4) / (x ** 4 - y ** 7) - (x ** 3 - 80 * x ** 7) - math.sqrt(
        (math.fabs(x) + y ** 4) / (68 * x ** 3 + 73 * x ** 5))


def foo2(x):
    if x < 138:
        return x ** 3 - x ** 4 / 62
    elif 218 > x >= 138:
        return 8 * x - x ** 2
    elif 218 <= x < 247:
        return x ** 6 - 86 * x ** 7
    else:
        return math.fabs(77 * x ** 4 + x ** 5) + math.tan(x ** 4)


def foo3(n, m):
    result_1 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result_1 += (i ** 7 - 62 * i ** 5)
    result_1 *= 21

    result_2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            result_2 += (i ** 4 - j ** 7)
    result_2 /= 42

    return result_1 + result_2


def foo4(n):
    if n == 0:
        return 8
    elif n == 1:
        return 7
    return 1 / 37 * foo4(n - 1) + math.sin(foo4(n - 2))


if __name__ == '__main__':
    print(foo1(11, 10))
    print(foo2(177))
    print(foo3(16, 70))
    print(foo4(12))
