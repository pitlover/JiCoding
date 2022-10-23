'''
6
DRRD
4
[1,2,3,4]
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
D
1
[]
'''
from collections import deque
# RR 무시하기
def solution(p, numbers):
    p = list(p)
    direction = 1 # D -> p[1:]
    numbers = deque(numbers)
    for a in p:
        if a == "R":
            direction *= -1
        else:
            if len(numbers) == 0 or numbers[0] == '':
                return "error"
            if direction == 1:
                numbers.popleft()
            else:
                numbers.pop()
    if direction == -1:
        numbers.reverse()

    return "[" + ",".join(numbers) + "]"

N = int(input())
for _ in range(N):
    p = input()
    _ = input()
    numbers = input()
    numbers =  "".join(numbers[1:-1]).split(",")
    print(solution(p, numbers))

