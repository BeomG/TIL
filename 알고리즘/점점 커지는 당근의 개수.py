T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst_carrot = list(map(int, input().split()))
    cnt = 1
    ans = 1
    for i in range(N-1):
        if lst_carrot[i+1] - lst_carrot[i] != 1:
            cnt = 1
        else:
            cnt += 1
            if cnt > ans:
                ans = cnt

    print(f'#{tc}', ans)