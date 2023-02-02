K = 4
N= 8
res = [-1] * N
nums = [0, 4, 1, 3, 1, 2, 4, 1]
counts = [0] * (K+1)
for num in nums:
    counts[num] += 1

print(counts)

for i in range(K):
    counts[i+1] = counts[i+1] + counts[i]

print(counts)

for i in range(N-1, -1, -1):
    num = nums[i]
    pos = counts[num] -1
    res[pos] = num
    counts[num] -= 1

print(res)