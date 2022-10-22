'''
10 4200 -> 1000*4 -> 200
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

N, K = map(int, input().split())
coin = []
for a in range(N):
    coin.append(int(input()))
coin = coin[::-1]

result = 0
for a in coin:
    if K // a > 0:
        result += (K // a)
        K -= (K//a * a)
print(result)