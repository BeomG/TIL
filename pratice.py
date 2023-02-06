#1. 4 X 3 이차원 배열 입력
M = 4
N = 3
'''
12 34 32
34 45 32
12 34 32
34 45 32
'''
l = [list(map(int, input().split())) for _ in range(M)]
# 0 col의 합
l[0][0] + l[1][0] + l[2][0] + l[3][0]
# i col의 합
l[0][i] + l[1][i] + l[2][i] + l[3][i]

for col in range(N):
    sumV = 0
    for row in range(M):
        sumV += l[row][col]


## i row의 합
# maxV = 0
# for row in range(M):
#     sumV = 0
#     for col in range(N):
#             sumV += l[row][col]
#     print(sumV)
#     if maxV < sumV:
#         maxV = sumV
# print(maxV)