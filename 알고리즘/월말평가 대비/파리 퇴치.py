T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mxV = 0
    for si in range(N):
        for sj in range(N):
            ans = 0
            for i in range(si,si+M):
                for j in range(sj,sj+M):
                    if 0 <= si <= N-M and 0 <= sj <= N-M:
                        ans += arr[i][j]
                        if mxV < ans:
                            mxV = ans
    print(f'#{tc} {mxV}')