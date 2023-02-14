def dfs(S, E):
    stack = []
    visited = [False] * (99+1)

    stack.append(S)
    visited[S] = True
    while stack:
        v = stack.pop()
        # if v == E:

        for w in lst[v]:
            if not visited[w]:
                if w == E:
                    return 1
                stack.append(w)
                visited[w] = True

    return 0
for tc in range(1, 11):
    T, V = map(int, input().split())
    S, G = 0, 99
    num = list(map(int, input().split()))
    lst = [[]*100 for _ in range(100)]
    for i in range(0, len(num), 2):
        v1 = num[i]
        v2 = num[i + 1]
        lst[v1].append(v2)

    print(f'#{tc} {dfs(S,G)}')