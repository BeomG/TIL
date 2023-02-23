T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = [0] + list(map(int, input().split()))
    for i in range(1, N + 1):
        while node[i // 2] > node[i]:
            node[i // 2], node[i] = node[i], node[i // 2]
            i //= 2

    p = N // 2
    ans = 0
    while p > 0:
        ans += node[p]
        p //= 2

    print(f'#{tc} {ans}')