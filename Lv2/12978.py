from collections import deque

def solution(N, road, K):
    answer = 0
    matrix = [[] for _ in range(N+1)]
    for a, b, point in road:
        matrix[a].append([b, point])
        matrix[b].append([a, point])
    
    queue = deque()
    queue.append([1, 0])
    print("queue", queue)
    result = [999999 for _ in range(N+1)]
    result[1] = 0
    visited = []
    
    print("-------")
    
    while queue:
        cur_val, cur_dis = queue.pop() # (1, 0)
        
        if cur_dis > result[cur_val]:
            continue
        
        for next_val, w in matrix[cur_val]:
            cost = cur_dis + w
            if result[next_val] > cost:
                result[next_val] = cost

                queue.append([next_val, cost])
        
    for x in result:
        if x<=K:
            answer +=1 
    return answer
