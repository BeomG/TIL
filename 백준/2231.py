import sys
N = int(sys.stdin.readline())

for i in range(1, N +1):
    temp = i
    sum_ = 0

    while i > 0:
        sum_ += i % 10
        i //= 10

    if N == temp + sum_:
        print(temp)
        break