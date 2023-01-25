frts = input().split(',')

lst_frts = []
for frt in frts:
    lst_frts.append(frt.lower())

rst_lst = []
for rst in lst_frts:
    rst_lst.append(rst.replace('rotten',''))

print(rst_lst)