for tc in range(1, 11):
    N = int(input())
    cnt = 0
    lst_rvs = []
    words_lst = [input() for _ in range(8)]
    for i in range(8):
        lst_rvs = []
        for j in range(8):
            lst_rvs.append(words_lst[j][i])
        for k in range(8-N+1):
            if lst_rvs[k:k+N] == lst_rvs[k:k+N][::-1]:
                cnt += 1

            if words_lst[i][k:k+N] == words_lst[i][k:k+N][::-1]:
                cnt += 1

    print(f'#{tc}', cnt)