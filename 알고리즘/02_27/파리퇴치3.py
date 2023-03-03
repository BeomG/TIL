T = int(input())
for tc in range(1, T+1):
    di_plus = [0, 1, 0, -1]
    dj_plus = [1, 0, -1, 0]
    di_x = [1, 1, -1, -1]
    dj_x = [1, -1, -1, 1]

    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mxPls = 0
    mxX = 0
    for i in range(n):
        for j in range(n):
            cntPls = arr[i][j]
            cntX = arr[i][j]
            for k in range(4):          # plus모양 최대합
                ni = i + di_plus[k]
                nj = j + dj_plus[k]
                if 0 <= ni < n and 0 <= nj < n:
                    cntPls += arr[ni][nj]
                    for _ in range(m-2):
                        ni += di_plus[k]
                        nj += dj_plus[k]
                        if 0 <= ni < n and 0 <= nj < n:
                            cntPls += arr[ni][nj]
                if cntPls > mxPls:
                    mxPls = cntPls

            for k in range(4):          # X 모양 최대합
                ni = i + di_x[k]
                nj = j + dj_x[k]
                if 0 <= ni < n and 0 <= nj < n:
                    cntX += arr[ni][nj]
                    for _ in range(m-2):
                        ni += di_x[k]
                        nj += dj_x[k]
                        if 0 <= ni < n and 0 <= nj < n:
                            cntX += arr[ni][nj]
                if cntX > mxX:
                    mxX = cntX
    if mxPls > mxX:
        mxX = mxPls

    print(f'#{tc} {mxX}')