T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    maxV = 0
    minV = 1000000
    for i in range(M-1, N):
        cnt = 0
        for l in range(i, i-M, -1):
            cnt += num[l]
        if cnt > maxV:
            maxV = cnt
        if cnt < minV:
            minV = cnt

    print(f'#{tc} {maxV - minV}')