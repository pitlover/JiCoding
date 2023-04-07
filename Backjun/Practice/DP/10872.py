'''
10
'''

DP = [1 for _ in range(13)]

for i in range(1, len(DP)):
    DP[i] = DP[i - 1] * i

print(DP[int(input())])
