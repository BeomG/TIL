import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 1
cnt_2 = 1
mxV = 0
mxV_2 = 0


for i in range(0, N-1):
    if lst[i-1] > lst[i] and lst[i] <= lst[i+1]:
        cnt = 1
    if lst[i] <= lst[i+1]:
        cnt += 1
        if cnt > mxV:
            mxV = cnt
    else:
        cnt = 1
        if lst[i] > lst[i+1]:
            cnt += 1
            if cnt > mxV:
                mxV = cnt
        else:
            cnt = 1

    if cnt > mxV:
        mxV = cnt

    if lst[i-1] < lst[i] and lst[i] >= lst[i+1]:
        cnt_2 = 1
    if lst[i] >= lst[i+1]:
        cnt_2 += 1
        if cnt_2 > mxV_2:
            mxV_2 = cnt_2
    else:
        cnt_2 = 1
        if lst[i] <= lst[i+1]:
            cnt_2 += 1
            if cnt_2 > mxV_2:
                mxV_2 = cnt_2
        else:
            cnt_2 = 1

if mxV < mxV_2:
    mxV = mxV_2

if len(lst) <= 2:
    print(len(lst))
else:
    print(mxV)