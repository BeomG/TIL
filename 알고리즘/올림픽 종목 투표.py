T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_A = list(map(int, input().split()))
    lst_B = list(map(int, input().split()))
    vote = [0] * N

    for j in range(M):
        min = 100
        for i in range(N):
            if lst_B[j] >= lst_A[i]:
                vote[i] += 1
                break
    max = 0
    x = 0
    for i in range(N):
        if vote[i] > max:
            max = vote[i]
            x = i

    print(f'#{tc} {x+1}')
