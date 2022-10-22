## 3진법 뒤집기
## Success

def three_ten(n):
    result = []
    while(n>2):
        result.append(n%3)
        n //= 3

    result.append(n)
    return result[::-1]

def ten_three(n):
    result = 0
    for a in range(len(n)):
        result += n[a] * (3**a)
    return result
def solution(n):
    temp = three_ten(n)
    answer = ten_three(temp)
    return answer



###
def best(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer