# 체육복
# Success
def solution(n, lost, reserve):
    answer = n - len(lost)
    # reserve.sort()
    
    # lost & reserve
    check = reserve[:]
    lost_check = lost[:]
    
    for a in reserve:
        if a in lost:
            answer += 1
            check.remove(a)
            lost_check.remove(a)
    
    for a in check[:]:
        if a-1 in lost_check[:]:
            answer += 1
            check.remove(a)
            lost_check.remove(a-1)
        elif a+1 in lost_check[:]:
            answer += 1
            check.remove(a)
            lost_check.remove(a+1)
            
    return answer
