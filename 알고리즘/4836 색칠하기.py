T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bin_lst = [[0] * 10 for _ in range(10)]
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                bin_lst[r][c] += color

    cnt = 0
    for r in range(10):
        for c in range(10):
            if bin_lst[r][c] == 3:
                cnt += 1
    print(f'#{tc} {cnt}')