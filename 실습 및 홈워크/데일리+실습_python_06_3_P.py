

count_vowels('apple') #=> 2
count_vowels('banana') #=> 3

def count_vowels(word):
    vowel_lst = ['a','e','i', 'o', 'u','y','w']
    cnt = 0
    for i in range(len(word)):
        if word[i] in vowel_lst:
            cnt += 1

    print(cnt)