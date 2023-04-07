'''
baekjoon
'''
s = list(input())
alpha_dict = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}

for i in range(len(s)):
    if alpha_dict.get(s[i]) == -1:
        alpha_dict[s[i]] = i

print(*alpha_dict.values())
