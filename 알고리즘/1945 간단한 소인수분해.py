num_lst = [2, 3, 5, 7, 11]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = [0] * 5
    for i in range(5):
        while N % num_lst[i] == 0:
            ans[i] += 1
            N = N // num_lst[i]
    print(f'#{tc} ans}')