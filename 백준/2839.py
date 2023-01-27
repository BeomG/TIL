def sugar(sugar):
    cnt = 1
    lst_3 = []
    lst_6 = []

    for i in range(5000):
        lst_3.append(3*i)
        lst_6.append(6*i)

    for a in range(5000):
        for b in range(5000):
            if sugar == lst_6[a] + lst_3[b]:
                print(b)
                
    
print(sugar(18))
