# [1차] 뉴스 클러스터링
# Success

def pre_process(arr):
    arr = arr.lower()
    temp, result = [], []
    for a in range(len(arr) - 1):
        result.append(arr[a] + arr[a + 1])

    for a in result:
        if a.isalpha():
            temp.append(a)

    return temp


def cal(str1, str2):
    intersec = 0
    total = len(str1) + len(str2)
    del_list1, del_list2 = [], []
    for i, a in enumerate(str1):
        if a in str2:
            del str2[str2.index(a)]
            intersec += 1

    union = total - intersec
    if union == 0:
        return 0
    return intersec / union


def solution(str1, str2):
    str1 = pre_process(str1)
    str2 = pre_process(str2)
    if str1 == str2:
        return 65536
    answer = cal(str1, str2)
    return int(answer * 65536)