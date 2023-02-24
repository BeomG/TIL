'''
# 전체 순회
def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N):     # 가능한 모든 시작위치
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0 <= i < N and 0 <= j < N:
                            cnt += arr[i][j]    # 집위치를 더하기(집 == 1)

                # 운영비용 보다 수익이 같거나 큰 경우 갱신
                if ((k*k) + (k-1) * (k-1)) <= cnt * M:
                    mx = max(mx, cnt)
    return mx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve_loop()
    print(f'#{tc} {ans}')
'''

'''
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]
def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N): # 가능한 모든 시작위치
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0<=i<N and 0<=j<N:
                            cnt += arr[i][j]    # 집위치를 더하기(집이 1이니 집 개수 추가)
                # 운영비용 보다 수익이 같거나 큰 경우 정답갱신
                # if ((k*k)+(k-1)*(k-1))<=cnt*M:
                if cost[k] <= cnt*M:
                    mx = max(mx, cnt)
    return mx
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # M: 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    ans = solve_loop()
    print(f'#{test_case} {ans}')
'''
'''
# bfs
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]
def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N): # 가능한 모든 시작위치
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0<=i<N and 0<=j<N:
                            cnt += arr[i][j]    # 집위치를 더하기(집이 1이니 집 개수 추가)
                # 운영비용 보다 수익이 같거나 큰 경우 정답갱신
                # if ((k*k)+(k-1)*(k-1))<=cnt*M:
                if cost[k] <= cnt*M:
                    mx = max(mx, cnt)
    return mx
 
def bfs(si,sj):
    q = []
    v = [[0]*N for _ in range(N)]
    old = 0
    mx = 0
 
    q.append((si,sj))
    v[si][sj]=1
    cnt = arr[si][sj]   # 시작좌표가 집이면 1, 아니면 0
 
    while q:
        ci,cj = q.pop(0)
        if old != v[ci][cj]:    # k값이 달라진경우
            old = v[ci][cj]
            if cost[v[ci][cj]]<=cnt*M:
                mx = max(mx, cnt)
 
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                cnt += arr[ni][nj]
    return mx
 
def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N): # 가능한 모든 시작위치
            mx = max(mx, bfs(si,sj))
    return mx
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # M: 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    # ans = solve_loop()
    ans = solve_bfs()
    print(f'#{test_case} {ans}')
'''
'''
# 범위기준 표시 후 확산 (아이디어)
cost = [((k*k)+(k-1)*(k-1)) for k in range(40)]
def solve_loop():
    mx = 0
    for si in range(N):
        for sj in range(N): # 가능한 모든 시작위치
            for k in range(1, 2*N):
                cnt = 0
                for i in range(si-k+1, si+k):
                    t = abs(si-i)
                    for j in range(sj-k+1+t, sj+k-t):
                        if 0<=i<N and 0<=j<N:
                            cnt += arr[i][j]    # 집위치를 더하기(집이 1이니 집 개수 추가)
                # 운영비용 보다 수익이 같거나 큰 경우 정답갱신
                # if ((k*k)+(k-1)*(k-1))<=cnt*M:
                if cost[k] <= cnt*M:
                    mx = max(mx, cnt)
    return mx
 
def bfs(si,sj):
    q = []
    v = [[0]*N for _ in range(N)]
    old = 0
    mx = 0
 
    q.append((si,sj))
    v[si][sj]=1
    cnt = arr[si][sj]   # 시작좌표가 집이면 1, 아니면 0
 
    while q:
        ci,cj = q.pop(0)
        if old != v[ci][cj]:    # k값이 달라진경우
            old = v[ci][cj]
            if cost[v[ci][cj]]<=cnt*M:
                mx = max(mx, cnt)
 
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                cnt += arr[ni][nj]
    return mx
 
def solve_bfs():
    mx = 0
    for si in range(N):
        for sj in range(N): # 가능한 모든 시작위치
            mx = max(mx, bfs(si,sj))
    return mx
 
def solve_idea():
    mx = 0
    home = []
    for si in range(N):
        for sj in range(N): # [1] 집의 모든 위치를 저장
            if arr[si][sj]==1:
                home.append((si,sj))
 
    # [2] 각 기준위치에서 거리별 집의 개수 누적하기
    for si in range(N):
        for sj in range(N): #
            dist = [0]*40
            # 거리별 집위치를 누적
            for ti,tj in home:
                t = abs(si-ti)+abs(sj-tj)+1
                dist[t]+=1
 
            for k in range(1, 40):
                dist[k]+=dist[k-1]
                if cost[k]<=dist[k]*M:
                    mx = max(mx, dist[k])
    return mx
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # M: 비용
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    # ans = solve_loop()
    # ans = solve_bfs()
    ans = solve_idea()
    print(f'#{test_case} {ans}')
'''