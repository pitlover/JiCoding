'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1
'''

n = int(input())


def sol(matrix, m):
    for i in range(m):
        for j in range(m):
            if i == 0 and j == 0:
                up, left = 0, 0
            else:
                up = 10 ** 9 if i < 1 else matrix[i - 1][j]
                left = 10 ** 9 if j < 1 else matrix[i][j - 1]
            matrix[i][j] = min(up, left) + matrix[i][j]

    return matrix[-1][-1]



for _ in range(n):
    m = int(input())
    matrix = [list(map(int, input().split(" "))) for _ in range(m)]
    result = sol(matrix, m)
    print(f"#{_ + 1} {result}")
