import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
lst.sort()
for i in lst:
    print(i)
