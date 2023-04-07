num_list = [int(input()) for _ in range(9)]
max_num = num_list[0]
max_idx = 0
for idx in range(len(num_list)):
    if max_num < num_list[idx]:
        max_idx = idx
        max_num = num_list[idx]
print(max_num)
print(max_idx+1)