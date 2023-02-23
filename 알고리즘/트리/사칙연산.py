def calc(c1, c2, op):
    if op == '+':
        return c1 + c2
    elif op == '-':
        return c1 - c2
    elif op == '*':
        return c1 * c2
    elif op == '/':
        return c1 // c2

for tc in range(1,11):
    N = int(input())
    node = [0] * (N+1)
    arr =[[]for _ in range(N+1)]
    for _ in range(N):
        lst = list(input().split())
        if len(lst) == 4:
            node[int(lst[0])] = lst[1]
            arr[int(lst[0])].append(int(lst[2]))
            arr[int(lst[0])].append(int(lst[3]))
        else:
            node[int(lst[0])] = int(lst[1])

    for i in range(N,0,-1):
        if node[i] == '+' or node[i] == '-' or node[i] == '*' or node[i] == '/':
            a, b = arr[i]
            node[i] = calc(node[a],node[b],node[i])

    print(f'#{tc} {node[1]}')