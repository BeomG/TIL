di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3

for i in range(N):
    for j in range(N):
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0 <= nj < N: