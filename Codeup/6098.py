'''
1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 2 1 0 1
1 0 0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''

matrix = [[] for _ in range(10)]
flag = 0

def matrix_update(x, y):
    if matrix[x][y] == 0:
        matrix[x][y] = 9
    elif matrix[x][y] == 2:
        matrix[x][y] = 9
        global flag
        flag = 1



for _ in range(10):
    matrix[_] = [int(x) for x in input().split()]

pos_x, pos_y = 1, 1

while True:
    matrix_update(pos_x, pos_y)
    if flag == 1:
        break
    elif (pos_y < 8) and matrix[pos_x][pos_y+1] in [0, 2]:
        pos_y += 1
    elif (pos_x < 8) and matrix[pos_x+1][pos_y] in [0, 2]:
        pos_x += 1
    elif (pos_x, pos_y) == (9, 9):
        break
    else:
        break
for _ in matrix:
    for __ in _:
        print(__, end=" ")
    print()
