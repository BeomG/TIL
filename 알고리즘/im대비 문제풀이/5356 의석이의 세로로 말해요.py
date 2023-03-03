T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            #if j < len(arr[i]):
            try:
                ans += arr[i][j]
            except:
                pass
    print(f'#{tc} {ans}')


    # #[1] 전치행렬 -> 틀림 (같은 길이 때만 사용 가능)
    # arr = [input() for _ in range(5)]
    # arr_t = list(zip(*arr))
    # ans = ''
    # for lst in arr_t:
    #     ans += "".join(lst)

