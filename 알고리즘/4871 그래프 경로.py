def dfs(S, E):
    stack = []
    visited = [False] * (V+1)

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

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[]*(V+1) for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)

    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S, G)}')

길찾기