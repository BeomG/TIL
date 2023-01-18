str_lst = input('문자열을 입력하세요. : ')

word = str_lst.split()

for i in range(1,len(word)):
    if word[i-1][-1] == word[i][0]:
        print('Pass')
    else :
        print('Fail')