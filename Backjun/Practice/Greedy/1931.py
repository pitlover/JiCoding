'''
13
11 13
13 14
1 4
0 6
5 7
3 5
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
# idea -> maybe smaller length & earlier?

N = int(input())
sched = []
for a in range(N):
    sched.append(list(map(int, input().split())))
sched = sorted(sched, key=lambda x: x[1], reverse=True)
sched = sorted(sched, key=lambda x: x[0], reverse=True)

result = 0
min_ = 2e9
for indx in range(N):
    if min_ >= sched[indx][1]:
        result +=1
        min_ = sched[indx][0]

print(result)