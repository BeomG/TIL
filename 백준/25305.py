import sys
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    nums = int(sys.stdin.readline())
    lst.append(nums)
lst.sort()
for i in lst:
    print(i)