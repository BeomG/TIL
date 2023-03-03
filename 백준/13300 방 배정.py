import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [[]for _ in range(7)]
for _ in range(N):
    S, Y = map(int, input().split())
    for i in range(7):
        if Y == i:
            arr[i].append(S)

cnt = 0
for i in arr:
    a = i.count(1)
    b = i.count(0)
    if 0 < a <= K:
        cnt += 1

    if a > K:
        cnt += a // K
        if a % K != 0:
            cnt += 1

    if 0 < b <= K:
        cnt += 1

    if b > K:
        cnt += b // K
        if b % K != 0:
            cnt += 1

print(cnt)