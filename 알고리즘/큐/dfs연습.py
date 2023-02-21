# def bfs(v, N):
#     visited = [0] * (N+1)   # visited 생성
#     q = [v]             # 큐 생성
#                         # 시작점 인큐
#     visited[v] = 1      # 시작점 인큐 표시
#     while q :       # 큐가 비어있지 않으면
#         t = q.pop(0)        # 디큐
#         print(t, end=' ')   # t에서 처리할 일
#         for v in adjL[t]: # t에 인접이고 방문한 적 없는 v
#             if visited[v] == 0:
#                 q.append(v)     # v에 인큐
#                 visited[v] = visited[t] +1 # v 인큐되었음을 표시
#```````````````````````````````````````````````````````````````````
def bfs(s):
    Q = []
    visited = [0] * (N+1)   # [0] * (N+1)으로 바꾸고
    Q.append(s)
    visited[s] = 1      # 1로 바꿈
    while Q:
        v = Q.pop(0)
        print(v)    # visited[v]도 같이 출력
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] =visited[v] + 1    #

def dfs(s):
    ST = []
    visited = [False] * (N+1)
    ST.append(s)
    visited[s] = True

    while ST:
        v = ST.pop()k
        print(v)

        for w in G[v]:
            if not visited[w]:
                ST.append(w)
                visited[w] = True
N = 7
s = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
lst = list(map(int, s.split()))
G = [[]for _ in range(N+1)]     # G = [[],[2, 3],[1, 4, 5] ...]
for idx in range(0, len(lst), 2 ):
    p1 = lst[idx]
    p2 = lst[idx+1]
    G[p1].append(p2)
    G[p2].append(p1)
print(G)