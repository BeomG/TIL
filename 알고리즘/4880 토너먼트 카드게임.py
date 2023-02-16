# l과 r 사이의 가위바위보정보를 기준으로 승자의 idx를 return
def game(l, r):
    if l == r:
        return r

    pivot = (l + r)//2
    lwinner = game(l, pivot)
    rwinner = game(pivot+1, r)

    return cal(lwinner, rwinner)