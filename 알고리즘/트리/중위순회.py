def inOrder(root):
    global ans
    if root:
        inOrder(int(tree[root][1]))
        ans += tree[root][0]
        inOrder(int(tree[root][2]))


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]
    ans = ''
    for _ in range(N):
        lst = input().split()
        node = int(lst[0])

        tree[node][0:len(lst)-1] = lst[1:]

    inOrder(1)
    print(f'#{tc} {ans}')