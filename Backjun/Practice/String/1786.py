'''
ABC ABCDAB ABCDABCDABDE
ABCDABD
'''
'''
Query에서 반복되는 부분 파악
idx ~ cur_idx 에 있는지 파악
'''


def chk_query(query: str):
    length = 0
    for a in range(len(query) // 2):
        if query[a] == query[-a]:
            length += 1


pattern = input()
query = input()

freq, idx = 0, 0
tmp_idx = 0
pos = []
while idx < len(pattern):
    if pattern[idx] == query[idx]:
        tmp_idx += 1

print(freq)
print(*pos)
