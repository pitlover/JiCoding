'''
1
2
'''
N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print(nums[0] ** 2)
else:
    nums.sort()
    print(nums[0] * nums[-1])
