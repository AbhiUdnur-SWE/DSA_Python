from ast import For


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

    if n == 0:
        return str(0)
    return to_binary(n // 2) + str(n % 2)


def flatten(arr):
    result = []

    for i in arr:
        if isinstance(i, list):
            result += flatten(i)
        else:
            result.append(i)

    return result


def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum


