T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = []
    for i in range(N):
        lst = [[1] for _ in range(i+1)]
        for j in range(N+1):
            for k in range(N+1):
               if k != 0 and j != k and j > 1 and k>1:
                   lst[j][k] = lst[j-1][k+1] + lst[j-1][k]
        print(lst)