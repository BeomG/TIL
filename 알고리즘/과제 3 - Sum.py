for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    row_max = 0
    col_max = 0
    max_V = 0
    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += arr[i][j]
        if row_max < sumV:
            row_max = sumV

    for j in range(100):
        sumV = 0
        for i in range(100):
            sumV += arr[i][j]
        if col_max < sumV:
            col_max = sumV

    sum_X = 0
    for i in range(100):
        sum_X += arr[i][i]
        if sum_X > max_V:
            max_V = sum_X

    sum_Y = 0
    for row in range(100):
        sum_Y += arr[row][99-row]
        if sum_Y > max_V:
            max_V = sum_Y

    rst = row_max
    if rst < col_max:
        rst = col_max

    if rst < max_V:
        rst = max_V

    print(f'#{tc} {rst}')
