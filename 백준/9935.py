import sys
wrd = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []

for i in wrd:
    stack.append(i)
    if i == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

ans = ''.join(stack)
if ans == '':
    print('FRULA')
else:
    print(ans)