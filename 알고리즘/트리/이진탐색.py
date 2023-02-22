def inOrder(rootidx):
    global cnt
    if  rootidx<= N and lst[rootidx]:
        inOrder(rootidx*2)
        cnt += 1
        Tree[lst[rootidx]] = cnt
        inOrder(rootidx*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    Tree = [0] * (N+1)
    cnt = 0
    for idx in range(len(lst)):
        lst[idx] = idx

    inOrder(1)
    print(f'#{tc}', Tree[1], Tree[N//2])