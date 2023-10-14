n = int(input())

nums = list(map(int, input().split()))

nums_set = set(nums)
nums_set = list(nums_set)
nums_set.sort()
nums_dict = {}
cnt = 0
for i in nums_set:
	nums_dict[i] = cnt
	cnt += 1
cnt = 0
for i in nums:
	nums[cnt] = nums_dict[i]
	cnt += 1

print(*nums)