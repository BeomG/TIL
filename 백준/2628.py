import sys
btm, high = map(int, sys.stdin.readline().split())
paper = [[1]*btm for _ in range(high)]
cut = int(sys.stdin.readline())
for _ in range(cut):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 :
        for i in range(btm):
            paper[y][i] = 0

    elif x == 1:
        for i in range(high):
            paper[i][y] = 0

print(paper)
