T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1):
        midIdx = i
        for j in range(i+1, N):
            if arr[midIdx] > arr[j]:
                midIdx = j
        arr[i], arr[midIdx] = arr[midIdx], arr[i]

    cnt = 1
    a = 0
    b = N -1
    ans = []
    for i in range(10):
        if cnt % 2 != 0:
            ans.append(arr[b])
            b -= 1
            cnt += 1
        else:
            ans.append(arr[a])
            a += 1
            cnt += 1

    print(f'#{tc}', *ans)