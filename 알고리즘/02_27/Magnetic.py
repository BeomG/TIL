for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ST = []
    for i in range(100):
        for j in range(100):
            if arr[j][i] == 1 or arr[j][i] == 2:
                ST.append(arr[i][j])