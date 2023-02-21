T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    si = sj = 0
    Q = []
    a = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                si = i
                sj = j
                visited[si][sj] = 1
                Q.append((si, sj))
    while Q:
        vR, vC = Q.pop(0)
        for k in range(4):
            ni = vR + di[k]
            nj = vC + dj[k]
            if 0 <= ni < N and 0 <= nj < N and miro[ni][nj] != 1:
                if not visited[ni][nj]:
                    Q.append((ni,nj))
                    visited[ni][nj] = visited[vR][vC] + 1
                    if miro[ni][nj] == 3:
                        a = visited[ni][nj] - 2

    print(f'#{tc} {a}')