def dfs(row, col):
    ST =[]
    visited = [[False] * N for _ in range(N)]

    ST.append((row, col))
    visited[row][col] = True
    while ST:
        # v = ST.pop()
        row, col = ST.pop() #v[0], v[1] 쓰기 귀찮
        for dr, dc in [(1,0), (-1,0), (0,1),(0,-1)]:
            newR = row + dr
            newC = col + dc
            if 0 <= newR < N and 0<= newC < N and ARR[newR][newC] != 1 and not visited[newR][newC]:
                if ARR[newR][newC] == 3:
                    return 1
                ST.append((newR, newC))
                visited[newR][newC] = True
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ARR = [list(map(int,input().strip())) for _ in range(N)]

    for row in range(N):
        if 2 in ARR[row]:
            col = ARR[row].index(2)
            break

    print(f'#{tc} {dfs(row, col)}')