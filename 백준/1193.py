import sys
N = int(sys.stdin.readline())

a_lst = [1]
a = 3
while a < 1500:
    if a % 2 == 0:
        for i in range(a-1, 0, -1):
            a_lst.append(i)
    else:
        for i in range(1, a):
            a_lst.append(i)
    a += 1

b_lst = [1]
b = 3
while b < 1500:
    if b % 2 != 0:
        for i in range(b-1, 0, -1):
            b_lst.append(i)
    else:
        for i in range(1, b):
            b_lst.append(i)
    b += 1

print(f'{a_lst[N-1]}/{b_lst[N-1]}')