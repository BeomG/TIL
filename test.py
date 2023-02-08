def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x) - ord('0')
    print(i,type(i))

def itoa(num):
    s = ''
    while num > 0:
        asc = (num%10) + ord('0')
        num = num // 10
        s = chr(asc) + s
    print(s, type(s))
