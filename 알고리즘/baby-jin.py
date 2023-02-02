s = '666456'
l = list(map(int, s))

counts = [0] * 12        # 총 숫자는 0~9까지 10개지만 뒤에 0추가로 out of range방지
for num in l:
    counts[num] += 1

# for i in range(10):       # for는 자동증가로 사용불가
i = 0
triple = 0
run = 0
while i < 10:
    if counts[i] >= 3:
        counts[i] -= 3
        triple += 1
        continue

    if counts[i] > 0 and counts[i+1] > 0 and counts[i+2]:
        counts[i] -= 1
        counts[i+1] -= 1
        counts[i+2] -= 1
        run += 1
        continue
    i += 1

print(run, triple)