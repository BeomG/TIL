import sys
N = list(map(int, input()))
N.sort(reverse=True)
for i in N:
   print(i,end='')