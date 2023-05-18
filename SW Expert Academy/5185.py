'''
3
4 47FE
5 79E12
8 41DA16CD
'''

n = int(input())

dic_hex = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"

}


def sol(string):
    string = list(string)
    result = []
    for a in string:
        result.append(dic_hex[a])
    return "".join(result)


for i in range(n):
    s, string = input().split(" ")
    result = sol(string)
    print(f"#{i+1} {result}")
