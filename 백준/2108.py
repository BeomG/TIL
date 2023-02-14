import sys
from collections import Counter
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

print(round(sum(nums)/len(nums)))

nums.sort()
print(nums[len(nums)//2])

cnt = Counter(nums).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(nums[-1]-nums[0])