# # 부분집합의 합 1
# def f(i, k, key):
#     if i == k:      # 하나의 부분집합 완성
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]  # 부분집합의 합
#         if s == key:    # 합이 key와 같은 부분집합 출력
#             return 1
#         else:
#             return 0
#             # for j in range(k):
#             #     if bit[j]:
#             #         print(A[j], end=' ')
#             # print()
#     else:
#         bit[i] = 1
#         if f(i+1, k, key):
#             return 1
#
#         bit[i] = 0
#         if f(i+1, k, key):
#             return 1
#         return 0
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 10
# bit = [0] * N
# f(0,N, key)
#

#
# # 부분 집합의 합 2
# def f(i, k, s, t): # i원소, k집합의 크기, s i-1까지 고려된 합, t목표값
#     global  cnt
#     if i == k:
#         if s == t:
#             # for j in range(k):            # 합이 key가 되는 배열
#             #     if bit[j] :
#             #         print(A[j],end=' ')
#             # print()
#             cnt += 1
#         return
#     else:
#         bit[i] = 1
#         f(i+1, k, s+A[i], t)    # A[i] 포함
#         bit[i] = 0
#         f(i+1, k, s, t)         # A[i] 미포함
#
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 50
# cnt = 0
# bit = [0] * N
#
# f(0, N, 0, key)
# print(cnt)      # 합이 key인 부분집합의 수


def partial(k, curS, key):
    # if curS > 10:
    #     return

    if k == N:
        print(bits,curS)
        if curS == key:
            return 1
        return 0

    bits[k] = 0
    if partial(k+1,curS,key):
        return 1
    bits[k] = 1
    if partial(k+1, curS+nums[k], key):
        return 1
    return 0

nums = [1, 2, 3, 4, 5]
N = 5
bits = [-1] * N
key = 100
partial(0,0, key)




# # 순열
# nums = [20, 30, 40]
# # goal : [20, 30, 40], [20, 40, 30] , [30, 20, 40], [30, 40, 20], [40, 20, 30], [40, 30 20]
#
# def per(k):
#
#     if k == N:
#         print(a)
#         # for i in range(N):
#         #     idx = a[i]
#         #     print(nums[idx], end=' ')
#         # print()
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             a[k] = i
#             per(k+1)
#             visited[i] = False
#
#
# N = 3
# a = [-1] * N
# visited = [False] * N
#
# per(0)