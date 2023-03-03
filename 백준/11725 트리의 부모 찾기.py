import sys
def dfs (s):
    global ans_lst
    ST = []
    visited = [False] * (N+1)
    ST.append(s)
    visited[s] = True
    if ST:
        for w in arr[s]:
            if visited[w]:
                ans_lst[w].append(s)
                ST.append(w)
                visited[w] = True


N = int(sys.stdin.readline())
arr = [[]for _ in range(N+1)]
ans_lst = [[] for _ in range(N+1)]
pos = 0
for _ in range(N-1):
    p, c = map(int, sys.stdin.readline().split())
    arr[p].append(c)
    arr[c].append(p)

for i in range(1, N+1):
    dfs(i)

print(ans_lst)