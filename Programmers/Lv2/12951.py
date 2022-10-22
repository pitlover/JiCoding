# JadenCase 문자열 만들기
# Success

def solution(s):
    s = s.lower()
    s = list(s)
    if s[0].isalpha():
        s[0] = s[0].upper()

    for index in range(1, len(s) - 1):
        if s[index + 1].isalpha() and s[index] == " ":
            s[index + 1] = s[index + 1].upper()

    return "".join(s)