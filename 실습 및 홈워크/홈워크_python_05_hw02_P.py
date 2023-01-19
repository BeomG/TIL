# fn_d(91) 
# 출력 예시 
# 101


# 1번
def fn_d(n):
    num = n
    for i in range(len(str(n))):
        num += int(str(n)[i])

    return num

print(fn_d(int(input())))

# 2번
# def is_selfnumber(n):
#     non_self_lst = []
#     if n < 10 and n % 2:
#         return print(n,"is selfnumber")
#     else:
        