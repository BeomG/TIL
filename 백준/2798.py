import sys

N, M = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))


while True:
    if len(lst) != N:
        break
    num_max = 0
    for a in range(N):
        for b in range(1,N):
            for c in range(2,N):
                num = lst[a] + lst[b] + lst[c]
                if a == b:
                    continue
                elif a == c:
                    continue
                elif b == c:
                    continue
                if num <= M and num_max < num:
                    num_max = num
    print(num_max)
    break