
test_lst = [1, 2, 3, 7, 4, 6, 5]
test_lst.sort()
print(test_lst)

# def check(x):
#     return x[1]

scores = [('eng', 88), ('sci', 90),('math', 80)]
# 정렬
# scores.sort(key=check)
scores.sort(key=lambda x: x[1])
print(scores)