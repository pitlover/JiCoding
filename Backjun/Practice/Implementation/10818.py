'''
5
20 10 35 30 7
'''
n = int(input())
nums = list(map(int, input().split()))

min_num = 1000001
max_num = -1000001
for idx in range(n):
    if max_num < nums[idx]:
        max_num = nums[idx]
    if min_num > nums[idx]:
        min_num = nums[idx]
print(min_num, max_num)