def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print(add(3, 4, 5, 6, 5, 6, 7, 8, 8))
print(calculate(add=3, multiply=5))
