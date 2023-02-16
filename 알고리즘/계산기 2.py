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

print(step1(input()))