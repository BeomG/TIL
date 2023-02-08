T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    if N in M:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)