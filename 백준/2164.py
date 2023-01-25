import sys

N = int(sys.stdin.readline())

lst = []
for i in range(1,N+1):
    lst.append(i)

while True:
    lst.remove(lst[0])
    num = lst.pop(0)
    lst.insert(len(lst)+1,num)
    if len(lst) == 1:
        print(lst[0])
        break