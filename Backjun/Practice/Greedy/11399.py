'''
5
3 1 4 3 2
'''
N = int(input())
P = list(map(int, input().split()))
P.sort() # 4 3 3 2 1
result = 0
for a in range(N):
    result += (N -a) * P[a]
print(result)
