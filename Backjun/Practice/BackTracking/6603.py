'''
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
'''


def dfs(results, idx):
    if len(results) == 6:
        print(*results)
        return

    for i in range(idx, k):
        results.append(arr[i])
        dfs(results, i + 1)
        results.pop()


while True:
    k, *arr = map(int, input().split())
    if k == 0:
        break

    dfs([], 0)
    print()
