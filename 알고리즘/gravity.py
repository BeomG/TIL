blocks = list(map(int, input().split()))

# res = [0] * len(blocks)
MaxV = 0
for i in range(len(blocks)):
    cnt = 0
    for j in range(i+1, len(blocks)):
        if blocks[i] > blocks[j]:
            cnt += 1

        if cnt > MaxV:
            MaxV = cnt

print(MaxV)

# maxV = 0
# for i in res:
#     if i > maxV:
#         maxV = i
#
# print(maxV)

