def fast_mul(x, y, temp=0):
    assert type(x) == int and type(y) == int and x > 0 and y > 0
    if x == 1:
        return y + temp
    elif x == 0 or y == 0:
        return 0
    if x % 2 == 1:
        temp += y
    return fast_mul(x//2, y*2, temp)


def fast_pow(x, y):
    assert type(x) == int and type(y) == int
    if y == 0:
        return 1
    elif y == 1:
        return x
    temp = x
    for i in range(y-1):
        temp = fast_mul(temp, x)
    return temp


def main():
    print(fast_mul(9, 100))
    print(fast_pow(4, 1))