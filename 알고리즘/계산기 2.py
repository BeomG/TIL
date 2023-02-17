def step1(exp):
    ST = []
    lst = []
    dct = {'+':1, '*':2 }
    for i in exp:
        if i.isdigit():
            lst.append(i)
        else:
            while ST and dct[i] <= dct[ST[-1]]:
                lst.append(ST.pop())
            ST.append(i)
    while ST:
        lst.append(ST.pop())

    return lst



