import sys
from collections import deque

def dfs(si,sj):
    ST = deque()
    visited = [[0] * N for _ in range(N)]
    ST.append(((si,sj)))
    visited[si][sj] = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    a = b = 0
    while ST:
        i, j = ST.pop()
        arr[i][j] = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                if not visited[ni][nj]:
                    ST.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1
                    a, b = ni, nj
    return visited[a][b]


N = int(sys.stdin.readline())
arr = [list(map(int, input())) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            print(dfs(i, j))
            cnt += 1
print(cnt)
