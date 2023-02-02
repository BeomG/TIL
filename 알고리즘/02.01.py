'''
55 7 78 12 42
5
for i : N-1 -> 1         # 각 구간의 끝
    for j : 0 -> i-1        # 비교할 왼쪽 원소
        if arr[j] > arr[j+1]
            arr[j] <-> arr[j+1]         # 큰 원소 오른쪽으로
'''
# arr = list(map(int, input().split()))
# N = int(input())
#
# for i in range(N-1, 0, -1):   # 각 구간의 끝
#     for j in range(i):   # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(*arr)

nums = [55, 7, 78, 12, 42]
N = 5
for i in range(N-1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)

# 자율실습 0번째 부터 채운다면, 작은 수에서 큰 수로 bubble 정렬