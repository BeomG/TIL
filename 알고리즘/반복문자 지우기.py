T = int(input())
for tc in range(1, T+1):
    stack = [0]
    word = list(input())
    for i in range(len(word)):
        if stack[-1] != word[i]:
            stack.append(word[i])
        else:
            stack.pop()

    print(f'#{tc} {len(stack)-1}')
