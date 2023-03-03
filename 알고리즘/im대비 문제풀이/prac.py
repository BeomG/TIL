n = int(input())
arr = []
for k in range(n):
    a, b = map(int, input().split())
    arr.append([a, b, k+1])

visited = [0] * n
ans = []
day = 0
def per(k, res):
    global day
    sumV = 0
    for i in range(len(res)):
        sumV += res[i][1]
    ans.append(sumV)

    for i in range(n):
        if day > 0:
            day -= 1
            continue
        if arr[i][0] + i > n:
            continue
        if res and i < res[-1][2] + res[-1][0] - 1:
            continue
        if not visited[i]:
            visited[i] = 1
            res.append(arr[i])
            day = arr[i][0] - 1
            per(k+1, res)
            res.pop()
            visited[i] = 0
            day = 0

per(0, [])
print(max(ans))