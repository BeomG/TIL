import sys

N = int(sys.stdin.readline())
arr = [[]for _ in range(N+1)]
for _ in range(N-1):
    p, c = map(int, sys.stdin.readline().split())
    arr[p] = c

print(arr)