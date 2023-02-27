def getCode(s):
    PATT = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

    return PATT[s]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    for row in range(N):
        if arr[row].count('1') > 0:
            st = M-1-arr[row][::-1].index('1') -55
            break

    codes = []
    for codei in range(8):
        codes.append(getCode(arr[row][st:st+7]))
        st += 7

    a = 0  # 짝수
    b = 0  # 홀수
    for i in range(0,len(codes)-1,2):
        a += int(codes[i])
        b += int(codes[i+1])

    if (a*3 + b)% 10 == 0:
        print(f'#{tc} {a+b}')
    else:
        print(f'#{tc}',0)