def solution(arr1, arr2):
    x_1, y_1 = len(arr1), len(arr1[0])
    x_2, y_2 = len(arr2), len(arr2[0])
    answer = [[0 for _ in range(y_2)] for _ in range(x_1)]
    tmp = 0
    for num1 in range(x_1):
        for num3 in range(y_2):
            for num2 in range(y_1):
                tmp += arr1[num1][num2] * arr2[num2][num3]
            answer[num1][num3] = tmp
            tmp = 0
    return answer
