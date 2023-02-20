T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 화덕의 크기, 피자 개수
    Q = []    # 화덕
    Ci =list(map(int, input().split())) # 뿌려진 치즈의 양
    nxt_P = N   # 넣고 남은 피자의 인덱스
    for i in range(N):
        Q.append((i+1,Ci[i]))   # 시작할 때 피자번호, 치즈양 넣기

    while Q :       # 오븐이 빌 때까지
        pzza = Q.pop(0) # 피자 꺼내서 피자 확인
        if pzza[1] // 2 == 0:   # 지즈양이 0이면 다시 안넣고
            if nxt_P < M:   # 피자 개수에 인덱스 맞추고
                Q.append((nxt_P+1, Ci[nxt_P]))  # 다음 피자 넣기
                nxt_P += 1  # 다음 피자 넣기 위해 인덱스 +1

        else:
            Q.append((pzza[0],pzza[1] // 2))     # 치즈양 0 아닐 시, 치즈 반절나누고 다시 넣기

    print(f'#{tc} {pzza[0]}')