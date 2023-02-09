lst = []
for _ in range(5):
    N = int(input())
    lst.append(N)
lst.sort()
print(sum(lst)//len(lst))
print(lst[len(lst)//2])