import sys
N = int(sys.stdin.readline())
bin_lst = []
maxV = 0
for _ in range(N):
    wrd = sys.stdin.readline()
    bin_lst.append(wrd)
    if len(wrd) > maxV:
        maxV = len(wrd)

bin_lst.sort()

wrd_lst = []
for i in range(1, maxV+1):
    for j in bin_lst:
        if len(j) == i:
            wrd_lst.append(j.strip())

print(wrd_lst[0])
for i in range(1, len(wrd_lst)):
    if wrd_lst[i] != wrd_lst[i-1]:
        print(wrd_lst[i])
