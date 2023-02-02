T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    cnt = [0] * 10
    for num in nums:
        cnt[num] += 1

    i_max = 0
    for i in cnt:
        if i > i_max:
            i_max = i

    max_card = 0
    for i in range(10):
        if cnt[i] == i_max:
            max_card = i

    print(f'#{tc} {max_card} {i_max}')