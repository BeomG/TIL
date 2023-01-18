# all_list_sum = ([[1],[2,3],[4,5,6],[7,8,9,10]])

# lst_sum = 0
# for i in all_list_sum:
#     for a in i:
#         lst_sum += a

# print(lst_sum)

def all_list_sum(value):
    lst_sum = 0
    for i in value:
        for a in i:
            lst_sum += a
    return lst_sum


print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))
