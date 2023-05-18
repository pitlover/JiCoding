'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''

from itertools import permutations

n = int(input())


def sol(m, matrix):
    cases = list(permutations(range(2, m + 1), m - 1))
    result = 10**9
    for case in cases:
        case = list(case)
        case.insert(0, 1)
        case.append(1)
        tmp = 0

        for i in range(len(case) - 1):
            a, b = case[i], case[i + 1]
            tmp += matrix[a - 1][b - 1]
        result = min(result, tmp)

    return result


for i in range(n):
    m = int(input())
    matrix = [list(map(int, input().split(" "))) for _ in range(m)]
    result = sol(m, matrix)
    print(f"#{i + 1} {result}")
