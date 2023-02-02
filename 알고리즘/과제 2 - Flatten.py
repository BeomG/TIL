for tc in range(1, 11):
    Dump = int(input())
    boxes = list(map(int, input().split()))

    cnt = 0
    while cnt <= Dump:
        mx = 0
        mn = 100
        mx_box = 0
        mn_box = 0
        for i in range(100):
            if boxes[i] > mx:
                mx = boxes[i]
                mx_box = i

            if boxes[i] < mn:
                mn = boxes[i]
                mn_box = i

        boxes[mx_box] -= 1
        boxes[mn_box] += 1
        cnt += 1

    print(f'#{tc} {mx - mn}')