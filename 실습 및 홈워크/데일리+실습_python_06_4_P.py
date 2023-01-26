entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter

print("입장 기록 많은 Top3")
for i in Counter(entry_record).most_common(3):
    print(i[0], i[1], "회")


print("\n출입 기록이 수상한 사람")
entry = Counter(entry_record)
exitt = Counter(exit_record)
entry.subtract(exitt)
name_entry = entry.keys()

num_entry = 0
for i in name_entry:
    if entry.get(i) > num_entry:
        name_entry = i
        num_entry = entry.get(i)
print(f'{name_entry}은 입장 기록이 {num_entry}회 더 많아 수상합니다.')


entry_2 = Counter(entry_record)
exitt.subtract(entry_2)
name_exit = exitt.keys()
num_exit = 0
for i in name_exit:
    if exitt.get(i) > num_exit:
        name_exit = i
        num_exit = exitt.get(i)
print(f'{name_exit}은 입장 기록이 {num_exit}회 더 많아 수상합니다.')

