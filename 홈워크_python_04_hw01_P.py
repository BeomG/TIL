words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

for i in range(1,len(words)):
    if words[i] == 'done':
        break
    elif words[i-1][-1] != words[i][0]:
        print(i+1,'번째 사람 탈락')
    elif words[i] in words[0:i]:
        print(i+1,'번째 사람 탈락')
        break