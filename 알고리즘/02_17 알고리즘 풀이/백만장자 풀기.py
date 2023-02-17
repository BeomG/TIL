T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    s = lst.pop()
    ans = 0
    for i in lst[::-1]:
        if s >= i:
            ans += s-i
        else:
            s = i

    print(f'#{tc} {ans}')