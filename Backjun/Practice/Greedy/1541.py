'''
000010-0020+30-40-50+60-70+80-0009
'''
math = input().split("-")
result = 0
if len(math) == 1:  # 0009 + 0009
    math_plus = math[0].split("+")
    for a in math_plus:
        result += int(a)

else:
    math_plus = math[0].split("+")
    for b in math_plus:
        result += int(b)
    for a in math[1:]:
        math_plus = a.split("+")
        for b in math_plus:
            result -= int(b)
print(result)
