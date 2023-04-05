# GCD
def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
      
def gcd(n, m):
    while m > 0:
        n, m = m, n % m
    return n
  
## 3 parameters ver.
def gcd(*args):
    def _gcd(n, m):
        while m > 0:
            n, m = m, n % m
        return n
    if len(args) < 2:
        return args[0]
    else:
        n = args[0]
        for m in args[1:]:
            n = _gcd(n, m)
        return n
      
# LCM
def lcm(n, m):  
    return n // gcd(n, m) * m
  
# 3 parameters ver.
def lcm(*args):
    def _lcm(n, m):
        return n * m //gcd(n, m)
    if len(args) < 2:
        return args[0]
    else:
        n = args[0]
        for m in args[1:]:
            n = _lcm(n, m)
        return n
