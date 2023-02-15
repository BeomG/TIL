def step1(exp):
    ST = []
    res = []
    for c in exp:
        if c.isdigit():
            res.append(c)
        else:
            if ST:
                res.append(ST.pop())
                ST.append(c)
            else:
                ST.append(c)
    while ST:
        res.append(ST.pop())
    return res

def step2(exp):
    ST = []
    for c in exp:
        if c.isdigit():
            ST.append(int(c))
        else:
            v1 = ST.pop()
            v2 = ST.pop()
            ST.append(v1 + v2)

    return ST[-1]
for tc in range(1, 11):
    N = int(input())
    exp = input()
    ARR = step1(exp)
    exp2 = ''.join(ARR)
    print(f'#{tc} {step2(exp2)}')