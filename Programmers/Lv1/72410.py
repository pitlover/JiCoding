## 신규 아이디 추천
## Success

def solution(new_id):
    new_id = new_id.lower()
    temp = ""
    for a in new_id:
        if a.isalpha() or a.isdigit() or a=="-" or a=="_" or a==".":
            temp += a
    new_id = temp
    temp = []
    print(new_id)
    for pointer in range(len(new_id)):
        if new_id[pointer] == ".":
            if pointer == 0:
                temp.append(new_id[pointer])
            elif new_id[pointer] != new_id[pointer-1]:
                temp.append(new_id[pointer])
        else:
            temp.append(new_id[pointer])
    new_id = "".join(temp)
    print(new_id)
    if new_id[0] == "." and len(new_id) == 1:
        new_id = "a"
    elif new_id[0] == ".":
        new_id = new_id[1:]
    print(new_id)
    if new_id[-1] == '.' and len(new_id) == 1:
        new_id = "a"
    elif new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) >=16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    if len(new_id) == 0:
        new_id = "a"
    if len(new_id) <= 2:
        while(len(new_id)<3):
            new_id += new_id[-1]
    answer = new_id
    return answer

import re
def best(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st