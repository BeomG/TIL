import random


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])



print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())

lst = []
random.shuffle()

rst = []
for i in range(0,len(lst)//2+1, 2):
    rst.append(i:i+2)
if len(lst)%2 == 1:
    #rst[-1].append(lst(-1))
    lst_data = rst[-1]
    lst.data.append(1st[-1])

print(rst)