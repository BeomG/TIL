import sys
S = sys.stdin.readline()
num = 0
cnt = 0
while num != int(S):
    if int(S) == 0:
        pass
    elif int(S) < 10:
        num = int(S[1] + S[1])
        cnt += 1
    else:
        num = str(int(S[0]) + int(S[1])) + S[1]
        cnt += 1
        
print(cnt)
    