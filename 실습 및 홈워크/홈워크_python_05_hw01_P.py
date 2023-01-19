# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
#경고 월요일입니다.
#{'년': 2015, '월': 8, '일': 31, '요일': '월요일'}
import calendar

year = int(input())

cldr = {'년':'','월':'','일':'','요일':''}
if calendar.isleap(year) == True:
    print('윤년입니다. 연도를 다시 입력해주세요.')
    year = int(input())
    cldr['년'] = year
elif calendar.isleap(year) == False:
    calendar.prcal(year)
    cldr['년'] = year

month = int(input())
cldr['월'] = month

day = int(input())
cldr['일'] = day

if calendar.weekday(year, month, day) == 0:
    cldr['요일'] = '월요일'
elif calendar.weekday(year, month, day) == 1:
    cldr['요일'] = '화요일'
elif calendar.weekday(year, month, day) == 2:
    cldr['요일'] = '수요일'
elif calendar.weekday(year, month, day) == 3:
    cldr['요일'] = '목요일'
elif calendar.weekday(year, month, day) == 4:
    cldr['요일'] = '금요일'
elif calendar.weekday(year, month, day) == 5:
    cldr['요일'] = '토요일'
else:
    cldr['요일'] = '일요일'

if calendar.weekday(year, month, day) == 0:
    print('경고 월요일입니다.')
print(cldr)