dV = 10

def decTobin(value):
    s = ''
    for j in range(3, -1, -1):
        s += '1' if value & (1<<j) else '0'

    print(s)
        # r = value & (1<<j)
        # if r != 0:
        #     print(1)
        # else:
        #     print(0)

# 16 진수 10진수로
def hexTodec(s):
    if s.isdigit():
        return int(s)
    else:
        return s - ord('A') + 10

# 16진수 2진수
def hexTobin(s):
    if s.isdigit():
        return decTobin(int(s))
    else:
        return decTobin(s- ord('A') + 10)

def hexTObin2(s)
    mapping = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

# 문자열 인트형으로 바꾸기
def atoi(s):
    res = 0
    for n in s:
        value = int(n)
        res = res*10 + value
    return res

# 2진수를 10진수로 변경
def binTohex(s):
    result = 0
    for i in s:
        result = result * 2 + int(i)
    return result