T = int(input())
for tc in range(1, T+1):
    words = list(input())
    stack = []
    for i in words:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

        elif i == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)

    if len(stack) > 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', 1)