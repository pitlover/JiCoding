# 2개 이하로 다른 비트
# Success

def compare(a, b):
    if len(a) > len(b):
        b = "0" * (len(a)-len(b)) + b
    elif len(a) < len(b):
        a = "0" * (len(b)-len(a)) + a
        
    result = 0   
    
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
            
        if result > 2:
            return -1
    
    return result
            

def solution(numbers):
    answer = []
    
    for data in numbers:
        num = bin(data)
        i = data + 1
        while True:
            tmp = bin(i)
                  
            if compare(tmp[2:], num[2:]) in [1, 2]:
                answer.append(i)
                break
            i+=1
    return answer
