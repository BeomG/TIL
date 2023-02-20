for tc in range(1, 11):
    _ = int(input())
    pswd = list(map(int, input().split()))
    cnt = 1
    while pswd[7] > 0:  # 비번 8번째 자리가 0보다 작을 때까지
        p = pswd.pop(0) # 첫 번째 비번 뽑아서
        p -= cnt    # cnt 만큼 빼고
        pswd.append(p)     # 마지막 인덱스에 다시 넣기
        cnt += 1    # 빼는 값 점점 크게
        if cnt > 5: # 빼는 값이 6이 될 때
            cnt = 1 # 다시 초기화

    pswd[-1] = 0    # 마지막 값이 음수가 될 수 있으므로 0으로 바꿔주기

    print(f'#{tc}', *pswd)