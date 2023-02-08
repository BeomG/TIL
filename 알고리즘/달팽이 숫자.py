T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    row = col = 0
    d = 0
    for i in range(1, N * N + 1):
        lst[row][col] = i
        newR = row + dr[d]
        newC = col + dc[d]
        if newR < 0 or newR >= N or newC >= N or lst[newR][newC] != 0:
            d = (d + 1) % 4
        row = row + dr[d]
        col = col + dc[d]

    print(f'#{tc}')
    for i in range(N):
        print(*lst[i])

