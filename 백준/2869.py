import sys
A, B ,V = map(int,sys.stdin.readline().split())

lgth = V - A
day = A - B

if lgth % day == 0:
    print(lgth // day + 1)
else:
    print(lgth // day + 2)