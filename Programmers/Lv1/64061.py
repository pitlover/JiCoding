# 크레인 인형뽑기 게임
# Success

def remove(box, answer):
    for a in range(len(box) - 1):
        if box[a] == box[a + 1]:
            answer += 2
            del box[a]
            del box[a]

            return box, answer, 1
    return box, answer, 0


def solution(board, moves):
    from collections import deque

    stacks = [deque() for _ in range(len(board))]
    for i, a in enumerate(board):
        for j, b in enumerate(a):
            if b != 0:
                stacks[j].append(b)

    box = []
    for b in moves:
        if len(stacks[b - 1]) > 0:
            item = stacks[b - 1].popleft()
            box.append(item)
    print(box)
    answer = 0
    temp = []
    flag = 1
    while (flag == 1 and len(box) != 0):
        box, answer, flag = remove(box, answer)

    return answer