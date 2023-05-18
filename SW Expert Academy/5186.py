'''
3
0.625
0.1
0.125
'''

n = int(input())


def sol(num):
    cnt, result = 1, ""

    while True:
        if num == 0:
            break

        if cnt >= 13:
            result = "overflow"
            break

        if 2 ** (-cnt) <= num:
            num -= 2 ** (-cnt)
            result += "1"
        else:
            result += "0"

        cnt += 1

    return result


for i in range(n):
    result = sol(float(input()))
    print(f"#{i + 1} {result}")