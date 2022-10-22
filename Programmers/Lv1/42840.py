# 모의고사
# Success

def solution(answers):
    answer = []
    result = []
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len1 = len(people1)
    len2 = len(people2)
    len3 = len(people3)
    score1, score2, score3 = 0, 0, 0
    
    for idx, a in enumerate(answers):
        if people1[idx%len1] == a:
            score1+=1
        if people2[idx%len2] == a:
            score2+=1
        if people3[idx%len3] == a:
            score3+=1
            
    result = [score1, score2, score3]
    
    max_ = max(result)
    print(result)
    for idx, a in enumerate(result):
        if a == max_:
            answer.append(idx+1)
    return answer
        
