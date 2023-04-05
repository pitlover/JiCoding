h, w = map(int, input().split())
n = int(input())
matrix = [[0 for _ in range(w)] for _ in range(h)]


def matrix_update(l, d, x, y):
    if d == 0: # row
        for a in range(y, y+l):
            matrix[x][a] = 1
    else: # col
        for a in range(x, x+l):
            matrix[a][y] = 1


for _ in range(n):
    l, d, x, y = map(int, input().split())
    matrix_update(l, d, x-1, y-1)
for _ in matrix:
    for __ in _:
        print(__, end=" ")
    print()
# 5 5
# 3
# 2 0 1 1
# 3 1 2 3
# 4 1 2 5

