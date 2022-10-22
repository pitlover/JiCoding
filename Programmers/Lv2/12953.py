# N개의 최소공배수
# Success

from math import gcd


def lcm(a, b):
    x = gcd(a, b)
    return a * b // x


def solution(arr):
    for a in range(len(arr) - 1):
        x = lcm(arr[a], arr[a + 1])
        arr[a + 1] = x

    return arr[-1]
