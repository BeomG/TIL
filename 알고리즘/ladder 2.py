# for tc in range(1, 11):
x = int(input())
ladder = [list(input().split()) for _ in range(100)]
dx = [0,0,1]
dy = [-1,1,0]       # 좌 우 하 이동
x = y = 0
nx = 0
ny = 0
for i in range(100):
    if ladder[0][i] == '1':     # 첫 줄이 1인 시작지점을 찾음
