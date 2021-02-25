
def f11(s):
    return [int(i) for i in s]


def f12(s):
    return len(set(s))


def f13(s):
    return s[::-1]


def f14(x, s):
    return [i for i, j in enumerate(s) if j == x]


def f15(s):
    return sum(s[::2])


def f16(s):
    return max(s, key=len)


# 19 символов!!!!!!!!!!
print("mcwuoocdwhe"[i::3])


def transpose(table):
    return list(zip(*table))


# как в kispython
def generate_groups():
    letter = ['K', 'В', 'Н']
    max_count = [25, 13, 10]
    result = []
    for i in range(len(letter)):
        for j in range(max_count[i]):
            result.append(letter[i] + str(j + 1))
    return result


print(type(f11(["1", "2", "3"])[0]))
print(f12([1, 2, 3, 4, 4, 3, 3]))
print(f13([1, 2, 3, 4, 4, 3, 3]))
print(f14(3, [1, 2, 3, 4, 4, 3, 3]))
print(f15([1, 2, 3, 4, 4, 3, 3]))
print(f16(["a", "", "bbb", "c", "dd"]))
print(transpose([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
print(generate_groups())




