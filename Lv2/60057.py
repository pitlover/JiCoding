# 문자열 압축
# Success

def sol(arr, n):
    tmp = []
    for a in range(0, len(arr), n):
        tmp.append(arr[a:a+n])
    ## 리스트 중복 빼기
    res = []
    res.append(tmp[0])
    count = 0
    list_ = []
    for i in range(1, len(tmp)):
        if tmp[i] != tmp[i-1]:
            res.append(tmp[i])
            list_.append(count)
            count = 0
        else:
            count += 1
        if i == len(tmp)-1:
            list_.append(count)
    result = 0
    for a in list_:
        if a != 0:
            result = result+ len(str(a+1))
    for a in res:
        result += len(a)
    return result
def solution(s):
    answer = len(s)
    for a in range(1, len(s) // 2 +1 ):
        tmp = sol(s, a)
        if tmp < answer:
            answer = tmp
    return answer