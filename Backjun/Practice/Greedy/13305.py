'''
4
2 3 1
5 2 4 1
'''
N = int(input())
cost = list(map(int, input().split()))
node = list(map(int, input().split()))

c =node[0]
result = 0
for idx, a in enumerate(node[:-1]):
    if node[idx] < c:
        c = node[idx]
    result += (c * cost[idx])
print(result)