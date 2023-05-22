'''
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8
'''
n = int(input())

for i in range(n):
    m = int(input())
    lists = list(map(int, input().split(" ")))
    lists.sort()
    print(f"#{i + 1} {lists[len(lists) // 2]}")
