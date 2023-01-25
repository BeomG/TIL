blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

bld_dict = {}
for i in blood_types:
    bld_dict[i] = blood_types.count(i)

print(bld_dict)