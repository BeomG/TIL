def isPair(input_s):
    stack = []
    for c in input_s:
        if c == '(' or '{':
            stack.append(c)''
        elif c == ')':
            if len(stack) == 0
                return False


            t = stack.pop(-1)
            if t != '(':
                return  False
    if len(stack) > 0
        return False
    return True