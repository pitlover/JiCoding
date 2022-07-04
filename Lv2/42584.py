# 주식가격
# Little Help

def solution(prices):
    answer = list(range(len(prices)))
    answer = answer[::-1]
    
    for index, data in enumerate(prices):
        for j in range(index+1, len(prices)):
            if prices[j] < data:
                answer[index] = j - index
                break
    
    return answer
