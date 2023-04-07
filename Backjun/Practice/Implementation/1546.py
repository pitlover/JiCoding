'''
3
40 80 60
'''
n = int(input())
nums = list(map(int, input().split()))

max_score = -1
sum_score = 0
for idx in range(n):
    if nums[idx] > max_score:
        max_score = nums[idx]
    sum_score += nums[idx]
print(sum_score * 100 / n / max_score)