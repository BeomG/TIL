import sys
from collections import deque

T = int(sys.stdin.readline())
for tc in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())
    impt = list(map(int, sys.stdin.readline().split()))
    Q = deque()
    dct = {}
    for i in range(N):
        Q.append(i)
        dct[Q[i]] = impt[i],Q[i]

    mxV = 0
    cnt = 0
    while Q:
        for i in Q:
            if dct[i][0] > mxV:
                mxV = dct[i][0]

        v = Q.popleft()
        if dct[v][0] == mxV:
            cnt += 1
            if dct[v][0] == mxV and dct[v][1] == M:
                print(cnt)
                break
            mxV = 0
            continue
        else:
            Q.append(v)


