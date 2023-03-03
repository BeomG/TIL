import sys
arr = [[0]* 100 for _ in range(100)]
num = int(input())
for _ in range(num):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1

cnt = 0
for i in arr:
    cnt += i.count(1)

print(cnt)