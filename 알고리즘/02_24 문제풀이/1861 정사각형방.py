def bfs(si, sj) :
    # [0] 생성
    q = []
    alst = []

    # [1] 초기데이터 삽입 등
    q.append((si, sj))
    v[si][sj] = 1
    alst.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)

        # 4/8, 미방문, 조건 맞으면! (1차이)
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and abs(arr[ci][cj]-arr[ni][nj])== 1:
                q.append((ni,nj))
                v[ni][nj] = 1
                alst.append(arr[ni][nj])
    return min(alst), len(alst)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    ans, cnt = N*N, 0
    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0:
                t, tcnt = bfs(si, sj)
                if cnt < tcnt or cnt == tcnt and ans > t:
                    ans, cnt = t, tcnt

    print(f'#{tc} {ans} {cnt}')