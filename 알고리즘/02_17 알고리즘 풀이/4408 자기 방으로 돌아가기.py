T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 200
    for _ in range(N):
        s,e = map(int,input().split())
        if s>e:
            s, e = e, s
        for j in range((s-1)//2 , (e-1) // 2+1):
            cnt[j] += 1
    ans = max(cnt)
    print(f'#{tc} {ans}')