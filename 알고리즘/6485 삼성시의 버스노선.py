T = int(input())
for tc in range(1, T+1):
    N = int(input())
    b_stop = [0] * 5001
    for _ in range(N):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            b_stop[i] += 1

    P = int(input())
    ans = []
    for _ in range(P):
        J = int(input())
        ans.append(b_stop[J])

    print(f'#{tc}', *ans)

