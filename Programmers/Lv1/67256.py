# 키패드 누르기
# Help

def cal_dis(num: int, pos: int):
    temp = abs(num - pos)
    if temp in [1, 3]:
        return 1
    elif temp in [2, 4, 6]:
        return 2
    elif temp in [5, 7, 9]:
        return 3
    elif temp in [8, 10]:
        return 4
    else:
        return 0


def solution(numbers, hand):
    answer = ''
    pos_l, pos_r = 10, 12
    L, R = [1, 4, 7], [3, 6, 9]
    for a in numbers:
        if a == 0:
            a = 11

        if a in L:
            answer += "L"
            pos_l = a
        elif a in R:
            answer += "R"
            pos_r = a
        else:  ## [2, 5, 8, 11]
            dis_l = cal_dis(a, pos_l)
            dis_r = cal_dis(a, pos_r)
            if dis_l < dis_r:
                answer += "L"
                pos_l = a
            elif dis_l > dis_r:
                answer += "R"
                pos_r = a
            else:
                if hand == "left":
                    answer += "L"
                    pos_l = a
                else:
                    answer += "R"
                    pos_r = a

    return answer