T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    si = sj =0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j
            for k in range(4):
                ni = si + di[k]
                nj = sj + dj[k]
                if 0 <= nj < N and 0 <= ni < N and arr[ni][nj] != 1:
                    if arr[ni][nj] == 3:
                        arr[ni][nj] = 1
                        print(1)
                        break
                else:
                    continue