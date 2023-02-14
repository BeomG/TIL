V = 7 + 1 #(0번 안씀)
# E =
# S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# S = list(map(int, input().split()))
# G =[[0] * V for _ in range(V)]
# for idx in range(0, len(S), 2):
#     v1 = S[idx]
#     v2 = S[idx + 1]
#     G[v1].append(v2)
#     G[v2].append(v1)

G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]

# def dfs(v):
#     stack = []
#     visited = [False] * V
#
#     stack.append(v)
#     visited[v] = True
#     print(v)
#     while len(stack) > 0:
#         for w in G[v]:
#             if visited[w]:
#                 visited[w] = True
#                 print(w)
#                 stack.append(v)
#                 v = w
#                 break
#         else:
#             v = stack.pop()

# def dfs(v):
#     stack = []
#     visited = [False] * V
#
#     stack.append(v)
#     while stack:
#         v = stack.pop()
#         if not visited[v]:
#             visited[v] = True
#             print(v)
#
#         for w in G[v]:
#             if not visited[w]:
#                 stack.append(w)

# # 재귀
# visited = [False] * V
#
# def dfsr(v):
#     print(v)
#     visited[v] = True
#     for w in G[v]:
#         if not visited[w]:
#             dfsr(w)

# 행렬렬
def dfs(v):
   stack = []
    visited = [False] * V

    stack.append(v)
    visited[v] = True
    while stack:
        v= stack.pop()
        print(v)
        # for w in G[v]:
        for w in range(V):
            if G[v][w] == 1 and visited[w]:
                stack.append(w)
                visited[w] = True