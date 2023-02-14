T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = []
    print(f'#{tc}')
    for i in range(n):
        lst.append(1)
        if i < 2:
            pass
        else:
            for j in range(i-1,0,-1):
                lst[j] += lst[j-1]
        print(*lst)