import sys
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    X = N // H +1
    Y = N % H
    if N % H == 0:
        Y = H
        X -= 1
    print((Y*100)+X)