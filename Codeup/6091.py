a, b, c = map(int, input().split())


def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n // gcd(n, m) * m

print(lcm(a, lcm(b, c)))

