import sys

def cal(i):
    global ans
    if arr[i][0] <= N-(i-1):
        ni = (arr[i][0])+i
        ans += arr[i][1]
        cal(ni)
    return

N = int(sys.stdin.readline())
arr = [[0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

mxV = 0
for k in range(1, len(arr)):
    ans = 0
    cal(k)
    if ans > mxV:
        mxV = ans

print(mxV)


