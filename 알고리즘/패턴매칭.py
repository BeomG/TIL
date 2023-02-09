T = 'This pattern matching algorithms'
def bmoor(P):
    lenP = len(P)
    lenT = len(T)
    skip = [lenP] * 128  # 아스키코드 수 만큼
    for i in range(lenP-1):
        t = P[i]
        skip[ord(P[i])] = lenP-1-i

    idxT = 0
    while idxT+lenP <= lenT:
        idxP = lenP-1
        while idxP >= 0 and T[idxT+idxP] == P[idxP]:
            idxP -= 1   # 뒤에서부터 확인하기때문에 -
        if idxP == -1:
            return idxT
        # asc = ord(T[idxT+idxP])
        # j = skip[asc]
        # idxT += j
        idxT += skip[ord(T[idxT+idxP])]

    return -1

def brute(P):
    lenP = len(P)
    lenT = len(T)
    idxT = 0
    for idxT in range(lenT-lenP+1):
        idxP = 0
        while idxP<lenP and T[idxT+idxP] == P[idxP]:
            idxP += 1
        if idxP == lenP:
            return idxT
    return -1
        # for idxP in range(lenP):
        #     if T[idxT+idxP] == P[idxP]:
        #         continue
        #     else:
        #         break


print(brute('patt'))
print(brute('pppp'))