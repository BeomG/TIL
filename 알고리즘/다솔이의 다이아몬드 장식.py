T = int(input())
for tc in range(1, T+1):
    word = list(input())
    lenW = len(word)
    lenD = (4*lenW+1)
    Dia = [['.' for _ in range(lenD)] for _ in range(5)]
    for j in range(2,lenD,4):
        Dia[0][j] = '#'
    for j in range(1,lenD,2):
        Dia[1][j] = '#'
    for j in range(0,lenD,4):
        Dia[2][j] = '#'
    for j in range(2,lenD,4):
        Dia[2][j] = word.pop(0)
    for j in range(1,lenD,2):
        Dia[3][j] = '#'
    for j in range(2,lenD,4):
        Dia[4][j] = '#'

    for i in Dia:
        ans = ''.join(i)
        print(ans)
