def fn_d(n):
    num = n
    for i in range(len(str(n))):
        num += int(str(n)[i])

    return num

print(fn_d(int(input())))