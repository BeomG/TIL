import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    a = ''
    b = ''
    x, *y = map(int, input().split())
    a = y
    i,*j = map(int, input().split())
    b = j

    cnt_a = []
    cnt_b = []
    for i in range(1, 5):
        cnt_a.append(a.count(i))
        cnt_b.append(b.count(i))

    p = 3
    while p > -1:
        if cnt_a == cnt_b :
            print('D')
            break

        if cnt_a[p] > cnt_b[p]:
            print('A')
            break
        elif cnt_a[p] == cnt_b[p]:
            p -= 1
        else:
            print('B')
            break