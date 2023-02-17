T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0,1,1,1,0,-1,-1,-1]
    dj = [1,1,0,-1,-1,-1,0,1]
    ans = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M :
                    if arr[ni][nj] < arr[i][j]:
                        cnt += 1
                        if cnt == 4:
                            ans += 1
                else:
                    continue
    print(f'#{tc} {ans}')