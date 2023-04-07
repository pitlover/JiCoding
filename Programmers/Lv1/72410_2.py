def solution(new_id):
    # 1
    new_id = list(new_id.lower())
    # 2-3
    for i in range(len(new_id)):
        if new_id[i] in [".", "_", "-"]:
            continue
        elif 48 <= ord(new_id[i]) <= 57 or 97 <= ord(new_id[i]) <= 122:
            continue
        else:
            new_id[i] = ""

    new_id = "".join(new_id)
    new_id = new_id.replace(".", " ").split(" ")
    tmp = []
    for a in new_id:
        if a != "":
            tmp.append(a)
    new_id = ".".join(tmp)
    # 4
    if len(new_id) == 0:
        new_id = 'a'
    # 5
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    # 6
    if len(new_id) == 1:
        new_id = new_id * 3
    elif len(new_id) == 2:
        new_id = new_id + new_id[-1]
    print(new_id)
    return new_id


solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
solution("=.=")
solution("123_.def")
solution("abcdefghijklmn.p")