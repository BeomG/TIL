def preorder(root):
    global cnt
    if root:
        preorder(leftC[root])
        preorder(rightC[root])
        cnt += 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    leftC = [0] * (E + 2)
    rightC = [0] * (E + 2)
    cnt = 0
    for idx in range(0,len(lst), 2):
        p = lst[idx]
        c = lst[idx + 1]

        if leftC[p] == 0:
            leftC[p] = c
        else:
            rightC[p] = c
    preorder(N)
    print(f'#{tc}', cnt)