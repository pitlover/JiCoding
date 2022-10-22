# 메뉴 리뉴얼
# Success 

from itertools import combinations
def solution(orders, course):
    result = dict()
    for data in orders:
        for num in course:
            tmp = list(combinations(data, num))
            for c in tmp:
                c = tuple(sorted(c, key=lambda x:x))
                if result.get(c, 0) == 0:
                    result[c] = 1
                else:
                    result[c] +=1
    tmp = []                
    for k, v in result.items():
        if v < 2:
            tmp.append(k)
    for a in tmp:
        del result[a]
    
    answer = []
    
    sorted_result = dict(sorted(result.items(), key=lambda x : x[1], reverse= True))
    max_ = 0
    
    for a in course: # 2, 3, 5
        max_ = 0
        for k, v in sorted_result.items():
            if len(k) == a:
                print(k, v, a, max_)
                if v >= max_:
                    max_ = v
                    answer.append("".join(list(k)))
  
    return sorted(answer)
