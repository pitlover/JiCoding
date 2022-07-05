# 구명보트
# Success

def solution(people, limit):
    answer = 0
    people.sort()
    pos = 0
    print(people)
    for a in range(len(people)-1, -1, -1):
        cur = people[a]
        if pos == a:
            return answer + 1
        if people[pos] + cur <= limit:
            pos += 1
        answer += 1
        
        if pos == a:
            return answer
    return answer
