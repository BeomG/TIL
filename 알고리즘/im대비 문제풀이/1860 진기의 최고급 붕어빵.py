T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = 'Possible'
    for t in lst:
        cnt += 1
        if cnt > (t//M)*K:  # 도착한 사람 수 > 만들어진 붕어빵
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}'
          f'')