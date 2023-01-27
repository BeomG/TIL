lst_a = []
lst_b = []

for i in range(3):
    a, b = map(int,input().split())
    lst_a.append(a)
    lst_b.append(b)

lst_a.sort()
lst_b.sort()

a = 0
if lst_a[0] == lst_a[1]:
    a = lst_a[2]
elif lst_a[1] == lst_a[2]:
    a = lst_a[0]

b = 0
if lst_b[0] == lst_b[1]:
    b = lst_a[2]
elif lst_b[1] == lst_b[2]:
    b = lst_b[0]

print(a, b)