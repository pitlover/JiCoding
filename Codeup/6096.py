matrix = [[] for _ in range(19)]


def flip(x, y):
    # row
    for x_ in range(19):
        flip_value(x, x_)
    # col
    for y_ in range(19):
        flip_value(y_, y)


def flip_value(x, y):
    matrix[x][y] = 0 if matrix[x][y] == 1 else 1


for _ in range(19):
    matrix[_] = [int(x) for x in input().split()]

n = int(input())
chang = []
for _ in range(n):
    x, y = map(int, input().split())
    chang.append((x, y))

for i in range(n):
    x, y = chang[i]
    flip(x - 1, y - 1)

for row in matrix:
    for row2 in row:
        print(row2, end=" ")
    print()

