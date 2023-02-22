import sys
from collections import deque

def bfs(si,sj):
    Q = deque()
    Q.append((si,sj))
    while Q:
        si, sj = Q.popleft()
        arr[si][sj] = 0
        if not visited[si][sj]:
            visited[si][sj] = True
            for k in range(4):
                ni = si + di[k]
                nj = sj + dj[k]
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                    Q.append((ni,nj))



T = int(sys.stdin.readline())
for tc in range(1, T+1):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    visited = [[False] * M for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)

