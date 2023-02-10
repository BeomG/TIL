for tc in range(1, 11):
    X = int(input())
    words_lst = [input() for _ in range(100)]
    maxV = 0
    for i in range(100):
        lst_rvs =[]
        for j in range(100):
            lst_rvs.append(words_lst[j][i])
            for k in range(100-i+1):
                if words_lst[i][i:j+1] == words_lst[i][i:j+1][::-1]:
                    if len(words_lst[i][i:j]) > maxV:
                        maxV = len(words_lst[i][i:j+1])

                if lst_rvs[i:j+1] == lst_rvs[i:j+1][::-1]:
                    if len(lst_rvs[i:j+1]) > maxV:
                        maxV = len(lst_rvs[i:j+1])
    print(maxV)