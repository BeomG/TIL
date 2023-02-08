def isPelindrome(s):
    lenS = 0
    for _ in s :
        lenS += 1

    s = s.strip()
    idx = 0
    while idx<lenS // 2 and s[idx] == s[lenS-1-idx]:
        idx += 1

    if idx == lenS//2:
        return 1
    return 0

def check():
    # 가로축 확인
    for row in range(N):
        for st in range(N-M+1):
            temp = ''
            for col in range(M):
                temp = temp + ARR[row][st+col]
            if isPelindrome(temp):
                return temp

    # 세로축 확인
    for col in range(N):
        for st in range(N-M+1):
            temp = ''
            for row in range(M):
                temp = temp + ARR[st+row][col]
            if isPelindrome(temp):
                return temp

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ARR = [input() for _ in range(N)]
    print(f'#{tc} {check()}')