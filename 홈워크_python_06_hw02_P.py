# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

words = input().split()
group_anagrams={}

for i in words:
    wrd = i
    i = sorted(i)
    i = ''.join(i)
    if i in group_anagrams:
        group_anagrams[i] += [wrd]
    else:
        group_anagrams[i] = [wrd]
print(group_anagrams.values())