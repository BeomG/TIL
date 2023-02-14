T = int(input())
for tc in range(1, T+1):
    num = int(input())
    lst = [0] * 31
    lst[1] = 1
    lst[2] = 3
    for i in range(3, 31):
        lst[i] = (lst[i-2])*2 + lst[i-1]
    
    ans = num // 10
    print(f'#{tc} {lst[ans]}')
