def step1(exp):
    exp = '(6+5(2-8)/2)'
    isp = {'+': 1, '-': 1, '': 2, '/': 2, '(': 0}  # 스택에 있는 문자열의 우선순위 지정 / 숫자가 클수록 우선순위가 높음
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}  # 문자열의 우선순위 지정 / 숫자가 클수록 우선순위가 높음

    stack = []

    for c in exp:
        if c.isdigit():
            print(c)

        elif c == ')':
            while stack and stack[-1] != '(':
                print(stack.pop())
            stack.pop()

        else:
            if stack and isp[stack[-1]] >= icp[c]:  # 여기서 stack이라고 쓰면 len(stack) > 0과 같은 의미디다
                print(stack.pop())
                stack.append(c)
            else:
                stack.append(c)
            while stack:  # 여기서 stack이라고 쓰면 len(stack) > 0 과 같은 의미이다.
                print(stack.pop())

step1('')