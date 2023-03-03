# 1)
# s = '0000000111100000011000000111100110000110000111100111100111111001100111'
# def binTodec(s): # 2진수 -> 10진수
#     result = 0
#     for i in s:
#         result = result * 2 + int(i)
#     return result
#
# for idx in range(0, len(s), 7):
#     print(binTodec(s[idx:idx+7]))


# 2)
def hexTodec(s): # 16진수 -> 10 진수
    if s.isdigit():
        return int(s)
    else:
        return ord(s) - ord('A') + 10

def decTobin(value):    # 10진수 -> 2진수
    S = ''
    for j in range(3,-1,-1):
        S += '1' if value & (1<<j) else '0'
    return S

def binTodec(s): # 2진수 -> 10진수
    result = 0
    for i in s:
        result = result * 2 + int(i)
    return result

s = '01D06079861D79F99F'
ans = ''
for i in s:
    ans += decTobin(hexTodec(i))

for idx in range(0, len(ans), 7):
     print(binTodec(ans[idx:idx+7]))
