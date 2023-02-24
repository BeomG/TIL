import sys
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
num = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

di = [0,1,1]
dj = [1,1,0]
cnt = 0
bingo = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        for x in range(5):
            for y in range(5):
                if num[i][j] == arr[x][y]:
                    arr[x][y] = 0
                    if i > 0:
                        j = 0
                        if arr[i][j] == 0:
                            cnt_0 = 0
                            for k in range(3):
                                ni = i + di[k]
                                nj = j + dj[k]
                                if 0 <= ni < 5 and 0 <= nj < 5:
                                    if arr[ni][nj] == 0:
                                        cnt_0 += 1
                                        ni += di[k]
                                        nj += dj[k]