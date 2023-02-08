T = int(input())
for tc in range(1, 11):
    lst = [list(map(int, input().split())) for _ in range(100)]
    n = 0
    dx = [0, 0, -1]
    dy = [-1, 1, 0]
    for j in range(100):
        if lst[99][j] == 2:
            num = j

    