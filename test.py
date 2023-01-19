def func2(a):
    v  = a+1
    return v
def func1(a):
    func2(a+1)
    return a

t = func1(3)
print(t)