lst = []
for i in range(1,31):
    lst.append(i)

check = []
for i in range(28):
    N = int(input())
    check.append(N)

for i in lst:
    if i not in check:
        print(i)