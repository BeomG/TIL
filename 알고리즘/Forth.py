def Forth(lst):
    stack = []
    for i in lst:
        if i.isdigit():
            stack.append(int(i))
        elif i == '.' and len(stack) == 1:
            return stack[0]
            break
        elif len(stack) == 1:
            return 'error'
        else:
            if i == '+':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 + v2)
            elif i == '-':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 - v2)
            elif i == '/':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 // v2)
            elif i == '*':
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(v1 * v2)
    if len(stack) > 2:
        return 'error'

T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())
    print(f'#{tc} {Forth(lst)}')