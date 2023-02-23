T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)
    for _ in range(M):
        nd, V = map(int, input().split())
        arr[nd] = V

    while arr[1] == 0:
        for i in range(1, N+1):
            if N % 2 != 0:
                if arr[i] == 0:
                    if arr[i*2] != 0 and arr[i*2+1] != 0:
                        arr[i] = arr[i*2] + arr[i*2+1]
            else:
                arr[N//2] = arr[N]
                if arr[i] == 0:
                    if arr[i * 2] != 0 and arr[i * 2 + 1] != 0:
                        arr[i] = arr[i * 2] + arr[i * 2 + 1]
    print(f'#{tc} {arr[L]}')