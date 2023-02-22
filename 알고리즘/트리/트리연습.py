# def preorder(root):
#     print(root)
#     if len(Tree[root]):
#         preorder(Tree[root][0])
#
#     if len(Tree[root]) == 2:
#         preorder(Tree[root][1])
#

# N = 13
# s = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
# lst = list(map(int, s.split()))
# # print(lst)
# Tree = [[]for _ in range(N+1)]
#
# for idx in range(0, len(lst),2):
#     p = lst[idx]
#     c = lst[idx + 1]
#
#     Tree[p].append(c)
#

# `````````````````````````````````````````````
# def preorder(root):
#     if root:
#         print(root)
#         preorder(leftC[root])
#         preorder(rightC[root])
# def findA(c):
#     while c != 0:
#         p = parent[c]
#         print(p)
#         c = p
#
#
# leftC = [0] * (N+1)
# rightC = [0] * (N+1)
# parent = [0] * (N+1)
#
# for idx in range(0, len(lst), 2):
#     p = lst[idx]
#     c = lst[idx+1]
#
#     parent[c] = p
#
#     if leftC[p] == 0:
#         leftC[p] = c
#     else:
#         rightC[p] = c
#
# # print(leftC)
# # print(rightC)
# print(parent)
# findA(10)
#`````````````````````````````````````````
def inOrder(rootIdx):
    if lst[rootIdx]:
        inOrder(rootIdx*2)
        print(lst[rootIdx])
        inOrder(rootIdx*2+1)

def findA(idx):
    while idx//2 >=1:
        idx = idx//2
        print(lst[idx])

lst = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'] + [0] * 100

inOrder(1)
