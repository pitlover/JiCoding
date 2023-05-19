'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''
n = int(input())
for i in range(n):
    result = sol(map(int, input().split(" "))
    print(f"#{i + 1} {result}")
