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
        return n * m // gcd(n, m)

    if len(args) < 2:
        return args[0]
    else:
        n = args[0]
        for m in args[1:]:
            n = _lcm(n, m)
        return n


def input_style():
    ''' Case1
    3
    1 2 3
    4 5 6
    7 8 9
    '''
    MAP = [list(map(int, input().split())) for _ in range(int(input()))]

    ''' Case2
    4 10 20 30 40
    3 7 5 12
    3 125 15 25
    '''
    N, *arr = map(int, input().split())
    ''' Case3 : string to list list(string)
    3           -> arr = 
    AAAA                    [['A', 'A', 'A', 'A']                  
    ABCA                    ['A', 'B', 'C', 'A']          
    AAAA                    ['A', 'A', 'A', 'A']]
    '''
    arr = [list(input()) for _ in range(int(input()))]
    ''' Case4 
    arr = [1, 2, 3, 4] -> print "1234" 
    '''
    print(" ".join(map(str, arr)))
    ''' Case5 
    arr = [1, 2, 3, 4] -> print "1 2 3 4" 
    '''
    print(*arr)
