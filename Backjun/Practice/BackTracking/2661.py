'''
7
'''

n = int(input())


def check(arr):
    for i in range(1, len(arr) // 2 + 1):
        if arr[-i:] == arr[-2 * i: -i]:
            return False
    return True


def dfs(arr):
    if len(arr) == n:
        print("".join(map(str, arr)))
        exit()

    for i in range(1, 4):
        arr.append(i)
        if check(arr):
            dfs(arr)
        arr.pop()


if n == 1:
    print(1)
    exit()

dfs([])
