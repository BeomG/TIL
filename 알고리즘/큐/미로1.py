for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().strip())) for _ in range(16)]
    Q = []
    visited = [[False] * 16 for _ in range(16)]
    si = sj = 0
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    ans = 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                si = i
                sj = j

    Q.append((si,sj))
    visited[si][sj] = True
    while Q:
        vi, vj = Q.pop(0)
        for k in range(4):
            ni = vi + di[k]
            nj = vj + dj[k]
            if arr[ni][nj] != 1 and visited[ni][nj] == False:
                Q.append((ni,nj))
                visited[ni][nj] = True
                if arr[ni][nj] == 3:
                    ans = 1

    print(f'#{tc} {ans}')