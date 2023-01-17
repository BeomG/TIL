num_2 = []
num_7 = []

for i in range(1000):
    if i % 2 == 0:
        num_2.append(i)
    elif i % 7 == 0:
        num_7.append(i)

print(sum(num_7) + sum(num_2))