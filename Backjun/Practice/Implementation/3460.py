'''
1
13
'''
t = int(input())
cases = [int(input()) for _ in range(t)]
for i in range(t):
    bi_string = bin(cases[i])[::-1]
    for idx in range(len(bi_string) - 2):
        if bi_string[idx] == '1':
            print(idx, end=" ")
    print()
