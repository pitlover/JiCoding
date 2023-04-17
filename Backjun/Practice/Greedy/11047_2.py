'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

result = 0
for i in coin[::-1]:
    result += (k // i)
    k -= (k // i) * i
print(result)
