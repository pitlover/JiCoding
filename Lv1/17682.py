# [1차] 다트게임
# Success

def get_pow(a):
    if a == "S":
        return 1
    elif a == "D":
        return 2
    else:
        return 3


def solution(dartResult):
    temp = []
    for a in range(1, len(dartResult) - 1):
        if (dartResult[a].isalpha() and dartResult[a + 1].isdigit()) or dartResult[a] in ["*", "#"]:
            temp.append(a + 1)
    dartResult = list(dartResult)
    for a in range(len(temp)):
        temp[a] += a
        dartResult.insert(temp[a], " ")
    list_ = "".join(dartResult).split()
    score_list = []
    for a in list_:
        if a[:2] == "10":
            score = 10 ** get_pow(a[2])
        else:
            score = int(a[0]) ** get_pow(a[1])

        if a[-1] == "#":
            score = -score
        elif a[-1] == "*":
            score *= 2
            print(score_list)
            if len(score_list) != 0:
                score_list[-1] *= 2
        score_list.append(score)
    return sum(score_list)


