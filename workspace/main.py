from Recursion import recursion_exs_basic
def power(base, exponent):
    if exponent == 1:
        return base
    base = base*base
    return power(base, exponent-1)
if __name__ == "__main__":

    print(power(2,3))
