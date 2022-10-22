# 제일 작은 수 제거하기
# Success

def solution(arr):
    if len(arr) == 1:
        return [-1]
    a = arr.index(min(arr))
    del arr[a]
    return arr