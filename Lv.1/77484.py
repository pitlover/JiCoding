## 로또의 최고 순위와 최저 순위
## Success
def cal(n):
    if n >= 2:
        return 7 - n
    return 6


def solution(lottos, win_nums):
    incorrect = []
    correct = []
    for a in lottos:
        if a in win_nums:
            correct.append(a)
        elif a != 0:
            incorrect.append(a)
    zeros = 6 - len(incorrect) - len(correct)
    print(zeros, incorrect, correct)
    max_ = cal(zeros + len(correct))
    min_ = cal(len(correct))
    return [max_, min_]
