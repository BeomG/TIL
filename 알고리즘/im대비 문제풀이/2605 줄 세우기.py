import sys

num = int(sys.stdin.readline())
stdnt = []
card = list(map(int, sys.stdin.readline().split()))
ans =[]

for i in range(1, num+1):
    stdnt.append(i)

for i in range(num):
    ans.insert(abs(card[i]-i),stdnt[i])

for i in ans:
    print(i, end=' ')