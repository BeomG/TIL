T = int(input())
for tc in range(1, T+1):
    check_lst = list(input())
    words_lst = list(input())
    maV = 0
    for i in range(len(check_lst)):
        cnt = 0
        for j in words_lst:
            if check_lst[i] == j:
                cnt += 1
            if cnt > maV:
                maV = cnt
    print(f'#{tc}', maV)
