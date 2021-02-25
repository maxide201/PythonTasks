import re


def f21(x):
    if x[3] == 2015:
        return 12
    elif x[3] == 2018:
        if x[1] == 'r':
            if x[4] == 'tla':
                if x[2] == 'hack':
                    return 0
                elif x[2] == 'tcl':
                    return 1
                elif x[2] == 'clips':
                    return 2
            elif x[4] == 'jsx':
                if x[2] == 'hack':
                    return 3
                elif x[2] == 'tcl':
                    return 4
                elif x[2] == 'clips':
                    return 5
            elif x[4] == 'sql':
                return 6
        elif x[1] == 'xproc':
            if x[2] == 'hack':
                if x[4] == 'tla':
                    return 7
                elif x[4] == 'jsx':
                    return 8
                elif x[4] == 'sql':
                    return 9
            elif x[2] == 'tcl':
                return 10
            elif x[2] == 'clips':
                return 11


def f22(x):
    d = x & 0xFE000000# 0b11111110000000000000000000000000
    c = x & 0x1F80000# 0b00000001111110000000000000000000
    b = x & 0x7C000# 0b00000000000001111100000000000000
    a = x & 0x3FFF# 0b00000000000000000011111111111111
    d = d >> 14
    c = c >> 19
    b = b >> 8
    a = a << 18
    x = a + b + c + d
    return x


def transpose(table):
    s = []
    size = len(table[0])
    for col in range(size):
        inner = []
        for row in range(len(table)):
            inner.append(table[row][col])
        s.append(inner)
    return s


def f23(table):
    checked = []
    for e in table:
        if e not in checked:
            checked.append(e)
    table = checked

    table = transpose(table)

    checked = []
    for e in table:
        if e not in checked:
            checked.append(e)
    table = checked

    table = transpose(table)

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] is not None:
                table[i][j] = table[i][j].replace('/', '.').replace('N', 'false').replace('Y', 'true').replace('@', '[at]').split(' ')[0]
    table.sort(key=lambda x: x[1])
    return table


