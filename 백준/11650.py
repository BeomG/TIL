import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append((a, b))

ans = sorted(lst, key = lambda x : ( x[1],x[0]))

for i in ans:
    print(i[0], i[1])