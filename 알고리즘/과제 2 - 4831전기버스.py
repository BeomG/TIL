T = int(input())
for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    lst_chrg = list(map(int, input().split()))

    curV = 0
    cnt = 0
    while curV < N:
        nextV = curV + K

        if nextV >= N:
            break

        while curV < nextV and nextV not in lst_chrg:
            nextV -= 1

        if curV == nextV:
            cnt = 0
            break

        curV = nextV
        cnt += 1

    print(f'#{tc} {cnt}')

'''
시작지점 0에서 +3을 해봤을 때 그 곳에 충전기가 있다면 그대로 go
없다면, 0~3 사이에 있는 충전기로 go하고, 그 인덱스를 다시 시작지점으로 설정
인덱스 11에 도착하거나 넘어갈 때까지 반복
'''