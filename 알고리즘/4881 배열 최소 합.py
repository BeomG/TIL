def per(r, curS):
    global mnV
    if N > r:
        if mnV < curS:
            return

    if r == N:
        if mnV > curS:
            mnV = curS

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(r+1, curS + arr[i][r])
            visited[i] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for N in range(N)]
    visited = [False] * N
    mnV = 100

    per(0, 0)
    print(f'#{tc}', mnV)