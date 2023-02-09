T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    print(f'#{tc}',len(A.replace(B,'a').strip()))
