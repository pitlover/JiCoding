def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        tmp = 0
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                tmp += 1
            else:
                tmp += 1
                break

        answer.append(tmp)

    answer.append(0)
    return answer


print(solution(prices=[1, 2, 3, 2, 3]))
print(solution(prices=[1, 2, 3, 2, 3, 5]))