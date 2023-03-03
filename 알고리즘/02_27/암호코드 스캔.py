def findCode(value):
    codes = {211: 0, 221: 1, 122: 2, 411: 3, 132: 4,
             231: 5, 114: 6, 312: 7, 213: 8, 112: 9}

    return codes[value]


def hexTobin():
    hexPATT = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    for rows in ARR:
        s = ''
        for hexV in rows:
            s += hexPATT[hexV]
        binARR.append(s)


TC = int(input())
# TC = 1
for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    ARR = [input().strip() for _ in range(N)]

    # 1. 16진수를 2진수로 만든다
    binARR = []
    hexTobin()

    ans = 0
    for row in range(1, N):
        # 2. 유의미한 코드가 있는 row와 col을 찾는다
        col = M * 4 - 1
        while col > 54:
            if binARR[row - 1][col] == '0' and binARR[row][col] == '1':
                codes = [-1] * 8
                for idx in range(8):
                    # 마지막 위치를 찾았음
                    cnt1 = 0
                    while binARR[row][col] == '1':
                        col -= 1
                        cnt1 += 1

                    cnt2 = 0
                    while binARR[row][col] == '0':
                        col -= 1
                        cnt2 += 1

                    cnt3 = 0
                    while binARR[row][col] == '1':
                        col -= 1
                        cnt3 += 1

                    while binARR[row][col] == '0':
                        col -= 1

                    ratio = min(cnt1, cnt2, cnt3)
                    code = findCode(cnt3 / ratio * 100 + cnt2 / ratio * 10 + cnt1 / ratio)
                    codes[1 - idx] = code

                sum1 = sum2 = 0
                for i in range(7):
                    if i % 2 == 0:
                        sum1 += codes[i]
                    else:
                        sum2 += codes[i]

                if (sum1 * 3 + sum2 + codes[7]) % 10 == 0:
                    ans += sum(codes)

            else:
                col -= 1

    print(f'#{tc} {ans}')