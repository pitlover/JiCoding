# 오픈채팅방
# Success

def change(final_name, name_list):
    for index, a in enumerate(name_list):
        name_list[index] = final_name.get(a)
    return name_list


def solution(record):
    answer = []
    name_list = []
    final_name = {}
    for a in record:
        if a[0] == "E":  # Enter
            _, user_id, name = a.split(" ")
            answer.append("님이 들어왔습니다.")
            name_list.append(user_id)
            final_name[user_id] = name
        elif a[0] == "L":  # Leave
            _, user_id = a.split(" ")
            answer.append("님이 나갔습니다.")
            name_list.append(user_id)

        else:  # Change
            _, user_id, change_name = a.split(" ")
            final_name[user_id] = change_name
    final = []

    name_list = change(final_name, name_list)
    for i in range(len(answer)):
        final.append(name_list[i] + answer[i])

    return final