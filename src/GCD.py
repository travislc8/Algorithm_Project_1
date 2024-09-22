# fuction for fast exponentiation
def fastExponetialMod(constant, power, mod):
    if power == 0:
        return 1
    if power % 2 == 0:
        temp = fastExponetialMod(constant, power//2, mod)
        return (temp*temp) % mod
    else:
        temp = fastExponetialMod(constant, power//2, mod)
        return constant * (temp**2 % mod) % mod


# recursive greatest common denominator function
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# recuresive function for extended greatest common denominator
def extendedGCD(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extendedGCD(b, a % b)
    return y, x - a // b * y, d
