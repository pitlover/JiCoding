'''
5
1 1 1 6 0
2 7 8 3 1
'''
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
print(sum(list(map(lambda a, b : a * b, A, B))))