T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst_pocket = [0] * 8
    lst_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        while N - lst_money[i] >= 0:
            lst_pocket[i] += 1
            N = N - lst_money[i]

    print(f'#{tc}')
    print(*lst_pocket)