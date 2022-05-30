## 신고 결과 받기
## Success

def solution(id_list, report, k):
    answer = []
    call = dict()
    warn = dict()
    final = dict()
    for a in id_list:
        call[a] = list()
        warn[a] = 0
        final[a] = 0

    for line in report:
        a, b, = line.split(" ")
        if not (b in call[a]):
            call[a].append(b)

    for id, black_list in call.items():
        for person in black_list:
            warn[person] += 1

    warn_list = []
    for key, value in warn.items():
        if value >= k:
            warn_list.append(key)

    for key, value in call.items():
        for per in warn_list:
            if per in value:
                answer.append(key)

    for a in answer:
        final[a] += 1

    answer = []
    for a in final.values():
        answer.append(a)
    return answer