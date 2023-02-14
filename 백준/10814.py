import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a, b = sys.stdin.readline().split()
    lst.append((a, b))

ans = sorted(lst, key = lambda x : ( x[0]))

for i in ans:
    print(i[0], i[1])