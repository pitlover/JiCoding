'''
5 0
-7 -3 -2 5 8
'''
n, s = map(int, input().split())
seq = list(map(int, input().split()))
result = 0
for i in range(1, 2 ** n):
    bin_i = list(bin(i))[2:]
    bin_i = list("0" * (n - len(bin_i)) + ''.join(bin_i))

    cnt = 0
    for ii in range(n):
        if bin_i[ii] == '1':
            cnt += seq[ii]
    if cnt == s:
        result += 1
    # print(bin_i, cnt)

print(result)
