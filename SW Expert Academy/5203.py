'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''
n = int(input())


def sol(datas):
    a_lists, b_lists = [], []
    for i in range(0, len(datas) - 1, 2):
        a_lists.append(datas[i])
        b_lists.append(datas[i + 1])

    result = 0

    a_trip_cnt = {i: 0 for i in range(-3, 13)}
    b_trip_cnt = {i: 0 for i in range(-3, 13)}

    for i in range(len(a_lists)):
        # a
        a_trip_cnt[a_lists[i]] += 1
        if (a_trip_cnt[a_lists[i]] == 3) or (a_trip_cnt[a_lists[i] - 1] > 0 and a_trip_cnt[a_lists[i] + 1] > 0) or (
                a_trip_cnt[a_lists[i] - 1] > 0 and a_trip_cnt[a_lists[i] - 2] > 0) or (
                a_trip_cnt[a_lists[i] + 2] > 0 and a_trip_cnt[a_lists[i] + 1] > 0):
            result = 1
            break

        # b
        b_trip_cnt[b_lists[i]] += 1
        if (b_trip_cnt[b_lists[i]] == 3) or (b_trip_cnt[b_lists[i] - 1] > 0 and b_trip_cnt[b_lists[i] + 1] > 0) or (
                b_trip_cnt[b_lists[i] - 1] > 0 and b_trip_cnt[b_lists[i] - 2] > 0) or (
                b_trip_cnt[b_lists[i] + 2] > 0 and b_trip_cnt[b_lists[i] + 1] > 0):
            result = 2
            break

    return result


for i in range(n):
    result = sol(list(map(int, input().split(" "))))
    print(f"#{i + 1} {result}")
