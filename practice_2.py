nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
c = [0, 1]
def partial(k, curS):
    if curS > 10:
        return

    if k == N:
        # print(a)
        # sumV = 0
        if curS == 10:
            for i in range(N):
                if a[i]:
                    print(nums[i], end=' ')
                    # sumV += nums[i]
            print('=>', curS)
        return

    a[k] = 0
    partial(k+1, curS)
    a[k] = 1
    partial(k+1, curS+nums[k])

    # for i in range(2):
    #     a[k] =c[i]
    #     partial(k+1)

a = [-1] * N
partial(0,0)