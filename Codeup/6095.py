n = int(input())
matrix = [[0 for _ in range(19)] for _ in range(19)]
for _ in range(n):
    x, y = map(int, input().split())
    matrix[x-1][y-1] = 1

for _ in matrix:
    for __ in _:
        print(__, end=" ")
    print()
