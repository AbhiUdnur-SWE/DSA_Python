def sum_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_digit(n // 10)


def power(x, n):
    if n == 1:
        return x
    return x * power(x, n - 1)


def gcp(x, y):
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y

    return gcp(y, x % y)


def to_binary(n):

    if n == 1:
        return str(1)
    return to_binary(n//2) + str(n % 2)
