from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights.append(0)
    answer, count, complete = 0, 0, 0
    queue = deque([None] * bridge_length)
    cur_weight = 0

    while complete < len(truck_weights):
        num = queue.popleft()
        if num != None:
            complete += 1
            cur_weight -= num
        answer += 1

        if count < len(truck_weights) and cur_weight + truck_weights[count] <= weight:
            queue.append(truck_weights[count])
            cur_weight += truck_weights[count]
            count += 1

        else:
            queue.append(None)
    return answer-1


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
