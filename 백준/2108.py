import sys
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
print(round(sum(nums)/len(nums)))
nums.sort()
print(nums[len(nums)//2])
cnt = 0
for i in range(len(nums)):
    if nums.count(nums[i]) > cnt:
        cnt = nums.count(nums[i])
print(cnt)
print(nums[-1]-nums[0])