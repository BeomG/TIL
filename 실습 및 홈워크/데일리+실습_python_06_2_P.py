grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

num_max = 0

for lst in grain_lst:
    if lst[1] > num_max:
        num_max = lst[1]

for lst in grain_lst:
    if lst[1] == num_max:
        print(lst[0])