N = int(input())
big = {}

for i in range(N):
    x, y = map(int,input().split())
    big[x] = y

big_keys = list(big.keys())
big_values = list(big.values())

for num in range(1,N):
    if big_keys[num-1] > big_keys[:num] and big_values[num-1] > big_values[:num]:
        print(num)