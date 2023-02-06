di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3

for i in range(N):
    for j in range(N):
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                print(i, j, ni, nj)