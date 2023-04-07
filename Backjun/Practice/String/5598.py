'''
MRL
'''
code = list(input())
for a in code:
    if a == 'A':
        print("X", end="")
    elif a == "B":
        print("Y", end="")
    elif a == "C":
        print("Z", end="")
    else:
        print(chr(ord(a) - 3), end="")
