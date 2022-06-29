# 위장
# Success

def solution(clothes):
    # sol 1
    items = {}
    for k, v in clothes:
        if items.get(v,0)==0:
            items[v] = [k]
        else:
            items[v].append(k)
    print(items)
    answer = 1
    for k, v in items.items():
        answer *= (len(v)+1)
    
    return answer -1
    
    # sol 2
    answer = 0
    name = list(items.keys())
    
    for a in range(1, 1 << len(items.keys())):
        tmp = []
        for b in range(len(items.keys())):
            if a & (1 << b):
                tmp.append(b)
        temp = 1
        for a in tmp:
            temp *= len(items[name[a]])
        answer += temp
        
    return answer
