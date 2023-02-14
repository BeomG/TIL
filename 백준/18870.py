import sys
N = int(sys.stdin.readline())
num_lst = list(map(int, sys.stdin.readline().split()))
ans_lst = num_lst
num_lst = set(num_lst)
num_lst = list(num_lst)
num_lst.sort()

ans = {}
for i in range(len(num_lst)):
      ans[num_lst[i]] = i

for i in ans_lst:
	print(ans.get(i), end= ' ')