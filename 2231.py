import sys
N = sys.stdin.readline()
num = []


for i in range(len(N)):
    num.append(N[i].replace(" ",""))
print(num)