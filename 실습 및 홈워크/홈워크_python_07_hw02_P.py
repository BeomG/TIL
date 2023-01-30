
def collatz(N):
    cnt = 0
    while N != 1:
        if N % 2 == 0:
            N = N // 2
            cnt += 1
        elif N % 2 != 0:
            N = (N * 3) + 1
            cnt += 1
    if cnt > 500:
        cnt = -1

    print(cnt)


collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
