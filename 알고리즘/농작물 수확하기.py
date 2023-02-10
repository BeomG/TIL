T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    lst = [0]
    cnt = 1
    for i in range(3, N+1):
        if i % 2 == 1:
            lst.append(cnt)
            cnt += 1

    A = lst[-2::-1]
    lst += A

    ans = []
    for i in range(N):
        for j in range(N//2-lst[i], N//2+1+lst[i]):
            ans.append(farm[i][j])
    print(f'#{tc} {sum(ans)}')