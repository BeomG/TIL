infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

num = 0
for i in infos:
    num += i.get('age')

print(num)