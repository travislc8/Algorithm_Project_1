def fastExponetialMod(constant, power, mod):
    if power == 0:
        return 1
    if power % 2 == 0:
        temp = fastExponetialMod(constant, power//2, mod)
        return (temp*temp) % mod
    else:
        temp = fastExponetialMod(constant, power//2, mod)
        return constant * (temp**2 % mod) % mod


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extendedGCD(a, b):
    if a < b:
        raise ValueError("variable a must be greater than variable b")
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extendedGCD(b, a % b)
    return y, x - a // b * y, d
