'''
3
5
20 23
17 20
23 24
4 14
8 18
10
14 23
2 19
1 22
12 24
21 23
6 15
20 24
1 4
6 15
15 16
15
18 19
2 7
11 15
13 16
23 24
2 14
13 22
20 23
13 19
7 15
5 21
20 24
16 22
17 21
9 24
'''

n = int(input())


def sol(lists):
    sched = [False] * 25
    result = 0
    for start, end in lists:
        flag = True
        for i in range(start, end):
            if sched[i] == True:
                flag = False
                break
        if flag == True:
            sched[start:end] = [True] * (end - start)
            result += 1
    return result


for i in range(n):
    m = int(input())
    lists = []
    for ii in range(m):
        s, e = map(int, input().split(" "))
        lists.append((s, e))
    lists = sorted(lists, key=lambda s: (s[1] - s[0], s[0]))
    result = sol(lists)

    print(f"#{i + 1} {result}")
