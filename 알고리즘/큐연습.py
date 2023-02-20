Q = []
no = 1
M = 20
Q.append(no)    # 1번줄, 마이주 1개
while Q:
    curNO, curMychu = Q.pop(0)    # 1번 받아감
    total += curMychu
    if total >= 20:
        break
    Q.append((curNO, curMychu+1) # 1번 줄, 마이쭈 증가
    no += 1
    Q.append(no)    # 2번 줄

# curNO, curMychu = Q.pop(0)   # 1번 받아감
# Q.append(curNO) # 1번 줄
# no += 1
# Q.append(no) # 3번 줄