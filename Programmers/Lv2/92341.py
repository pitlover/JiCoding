# 주차 요금 계산
# Success

def solution(fees, records):
    car = dict()
    time_period = dict()

    for a in records:
        time, ID, flag = a.split(" ")
        print(time, ID, flag)
        if ID not in time_period.keys():
            time_period[ID] = 0
        hour, mint = map(int, time.split(':'))
        time = hour * 60 + mint
        if flag == "IN":
            car[ID] = {"IN": time, "OUT": 23 * 60 + 59, "is_finish": 0}
        else:
            car[ID]["OUT"] = time
            period = car[ID]["OUT"] - car[ID]["IN"]
            time_period[ID] += period
            car[ID] = {"IN": 0, "OUT": 0, "is_finish": 1}

    import math
    for key, values in car.items():
        if values["is_finish"] == 0:
            period = car[key]["OUT"] - car[key]["IN"]
            time_period[key] += period
    answer = dict()
    for key, values in time_period.items():
        print(fees)
        if values <= fees[0]:
            answer[key] = fees[1]
        else:
            answer[key] = fees[1] + math.ceil((values - fees[0]) / fees[2]) * fees[3]
    name = []
    result = []
    print(answer)
    for a in answer.keys():
        name.append(a)
    for a in sorted(name):
        result.append(answer[a])
    return result