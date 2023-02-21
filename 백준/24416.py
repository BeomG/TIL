def fibo(n):
    fi[1] = 1
    fi[2] = 1
    cnt = 0
    for i in range(3, n+1):
        fi[i] = fi[i-1] + fi[i-2]
        cnt +=1

    return fi[n], cnt

n = int(input())
fi = [0] * (n+1)
fi[0] = 0
fi[1] = 1

a = 0
b = 0
for i in range(n+1):
    a, b = fibo(n)

print(a, b)