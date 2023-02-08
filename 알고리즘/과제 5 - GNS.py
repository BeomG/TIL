numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    N, M = input(). split()
    words = list(input().split())
    lst = [[]for _ in range(10)]
    for word in words:
        for i in range(10):
            if numbers[i] == word:
                lst[i].append(numbers[i])

    print(f'#{tc}')
    for i in lst:
        ans = ' '.join(i)
        print(ans, end=' ')


