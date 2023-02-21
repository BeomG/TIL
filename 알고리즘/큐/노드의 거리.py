T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[]for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    S, G = map(int, input().split())
    Q = []
    visited = [0] * (V+1)
    Q.append(S)
    visited[S] = 0
    ans = 0
    while Q:
        v = Q.pop(0)
        for w in lst[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
                if w == G:
                    ans = visited[w]

    print(f'#{tc}', ans)

