year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print('윤년')
elif year % 400 == 0:
    print('윤년')
