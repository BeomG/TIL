import sys
while True:
    N = int(sys.stdin.readline())
    prime_num = []
    if N == 0:
        break
    else:
        for i in range(N+1, (2*N)+1):
            condition = True
            if i == 1 : continue
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    condition = False
                    break
            if condition:
                prime_num.append(i)

    print(len(prime_num))