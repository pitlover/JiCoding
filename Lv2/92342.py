# 양궁대회
# Success

def solution(n, info):
    info = info[::-1]
    max_diff= -1
    cur_answer = -1
    for a in range(1, 1 << 10):
        index_list = []
        for b in range(10):
            if a & (1 << b):
                index_list.append(b)
        if len(index_list) > n:
            continue
        ### check
        is_over = 0
        peach_list = [0 for _ in range(10)]
        for a in index_list: # 2, 4, 6
            peach_list[a] += (info[a+1] + 1)
            is_over += (info[a+1] + 1)
        if is_over > n:
            continue
        
        peach_list.insert(0, n-is_over)
        lion_score, peach_score = 0, 0
        for a in range(11):
            if peach_list[a] == 0 and info[a] == 0:
                continue
            if peach_list[a] >= info[a]:
                peach_score += a
            else:
                lion_score += a
        if max_diff < peach_score - lion_score:
            max_diff = peach_score - lion_score
            cur_answer = peach_list
        elif max_diff == peach_score - lion_score:
            print("------")
            print("peach", peach_score, "lion", lion_score)
            print("cur_ans", cur_answer)
            print("peach_ans", peach_list)
            for a in range(11):
                if cur_answer == -1:
                    cur_answer = peach_list
                    break
                elif peach_list[a] > cur_answer[a]:
                    cur_answer = peach_list
                    break
                elif peach_list[a] < cur_answer[a]:
                    break
                else:
                    continue
            print("update_ans", cur_answer)
    if max_diff == -1 or max_diff == 0:
        return [-1]
    return cur_answer[::-1]
