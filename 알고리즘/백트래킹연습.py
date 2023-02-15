NUMS = [1, 2, 3]
N = 3
a = [-1] * N
def construct_candidates(c, k):
    pos = 0
    for i in range(N):
        if i not in a[0:k]:
            c[pos] = i
            pos += 1
    return pos
    # c[0] = 0
    # c[1] = 1
    # return 2

def backtrack(a, k):
    c = [-1] * N # 후보군 숫자만큼
    if k == N:
        print(a)
        return

    nc = construct_candidates(c, k)
    for i in range(nc):
        a[k] = c[i]
        backtrack(a, k+1)

backtrack(a, 0)