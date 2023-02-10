T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))
    a1 = [[0] * N for _ in range(N)] # 90도
    a2 = [[0] * N for _ in range(N)]
    a3 = [[0] * N for _ in range(N)]

    # # [1]회전각도에 따른 위치값을 저장
    # for i in range(N):
    #     for j in range(N):
    #         a1[i][j] = arr[N-1-j][i]
    #         a2[i][j] = arr[N-1-i][N-1-j]
    #         a3[i][j] = arr[j][N-1-i]
    # print(f'#{tc}')
    # for a, b, c in zip(a1, a2, a3):
    #     print(f'{"".join(a)} {"".join(b)} {"".join(c)}')

    # [2]전치배열과 읽는 방향에 따른 처리
    print(f'#{tc}')
    for i in range(N):
        print(f'{"".join(arr_t[i][::-1])} {"".join(arr[N-1-i][::-1])} {"".join(arr_t[N-1-i])}')