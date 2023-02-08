def binary_search(end, page):
    start = 1
    mid = end//2
    cnt=0
    while(1):
        cnt += 1
        if mid == page:
            return cnt
        elif mid > page:
            end = mid
        elif mid < page:
            start = mid
        mid = (end + start) // 2

T = int(input())
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())

    t_a = binary_search(p, a)
    t_b = binary_search(p, b)
    if t_a == t_b:
        print(f'#{tc}', 0)
    elif t_a > t_b:
        print(f'#{tc}', 'B')
    else:
        print(f'#{tc}', 'A')