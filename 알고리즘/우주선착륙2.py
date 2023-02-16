T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) * N for _ in range(M)]
    row = col = 1
    dr = [1,]
    dc = [0,]