T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    m = N//2
    #[2] 범위
    s = e = m
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]
        # s, e 조정
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    #[1] 규칙성
    # for i in range(N):
    #     for j in range(abs(m-i), N-abs(m-i)):
    #         ans += arr[i][j]
    
    print(f'#{tc} {ans}')