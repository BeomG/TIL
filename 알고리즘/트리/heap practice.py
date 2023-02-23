# import heapq
# # 최소값 뽑기 하나씩
# h = []
# lst = [15, 4, 13, 20, 11, 19]
# for item in lst:
#     heapq.heappush(h, item)
#
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
def enq(item):
    global last
    last += 1
    tree[last] = item
    c = last
    p = c//2
    while p >= 1 and tree[c] > tree[p]:    # 힙이 깨졌으면
        tree[c], tree[p] = tree[p],tree[c]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1
    p = 1
    c = p * 2
    while c<=last:  # p가 자식노드가 하나라도 있는 동안
        if c+1 < last and tree[c] < tree[c+1]:#오른쪽 자식 노드가 있으면 and 오른쪽 노드가 더 크면
                c += 1

        if tree[p]< tree[c]: # heap이 깨졌으면
            tree[c], tree[p] = tree[p],tree[c]
            p = c
            c = p*2
        else:
            break

    return tmp

tree = [0] * 100
last = 0
lst = [15, 4, 13, 20, 11, 19]
for item in lst:
    enq(item)
    print(tree)