# K번째 수
# Success

def sol(arr, k):
    arr.sort()
    return arr[k - 1]


def solution(array, commands):
    answer = []
    for a, b, c in commands:
        temp = array[a - 1:b]
        x = sol(temp, c)
        answer.append(x)
    return answer