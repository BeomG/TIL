import sys
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())   #층
    n = int(sys.stdin.readline())   #호
    lst_0 = [x for x in range(1, n+1)]  # 0층 리스트
    for k in range(k):      #층 수 만큼 반복
        for i in range(1,n):
            lst_0[i] += lst_0[i-1]
    print(lst_0[-1])


