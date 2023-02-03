T = int(input())
for tc in range(1, T+1):
    num = list(map(int, input()))
    num_len = 0
    for i in num:
        if i >= 0:
            num_len += 1
    cnt = 0
    if num[0] == 1:
        cnt += 1
    for i in range(num_len-1, 0, -1):
        if num == [1, 0]:
            cnt = 1
        elif num[i] != num[i-1]:
            cnt += 1

    print(f'#{tc} {cnt}')