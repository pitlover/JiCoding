'''
5
4 1 5 2 3
5
1 3 7 9 5
'''
n = int(input())
a = map(int, input().split())
m = int(input())
case = map(int, input().split())

bank = {}
for i in a:
    bank[i] = True

for i in case:
    if bank.get(i) == None:
        print(0)
    else:
        print(1)
