arr = list(range(1, 13))
R = len(arr)
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    rst = 0
    for n in range(0, 1 << R):
        cnt = 0
        num = 0
        for j in range(R):
            r = n & (1 << j)
            if r != 0:
                cnt += 1
                num += arr[j]
        if cnt == N and num == K:
            rst += 1

    print(f'#{tc} {rst}')