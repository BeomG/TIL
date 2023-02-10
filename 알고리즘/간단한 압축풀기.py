T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = 0         # 리스트 만들 갯수
    C_lst = []      # 받은 ci를 ki만큼 넣을 리스트
    for i in range(N):
        Ci, Ki = input().split()
        C_lst.append(Ci * int(Ki))
        num += int(Ki)

    ans_lst = [[] for _ in range((num // 10) + 1)]
    A = ''
    for i in C_lst:
        A += i

    lst = list(A)
    cnt = 0
    for i in lst:
        ans_lst[cnt].append(i)
        if len(ans_lst[cnt]) == 10:
            cnt += 1

    print(f'#{tc}')
    for i in ans_lst:
        print(''.join(i))