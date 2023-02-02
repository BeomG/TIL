T = int(input())
for t in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    maxV = 0
    minV = 1000000
    for i in range(N):
        if ai[i] > maxV:
            maxV = ai[i]

        if ai[i] < minV:
            minV = ai[i]

    print(f'#{t} {maxV - minV}')