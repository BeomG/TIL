def insert(item):
    pos = 1
    while tree[pos] != 0:
        if tree[pos] == item:
            return

        if tree[pos] < item:  # 넣으려는게 더 크면
            pos = pos * 2 + 1
        else:
            pos = pos * 2
    tree[pos] = item

def find(key):
    pos = 1
    while tree[pos] != 0:
        if tree[pos] == key:
            return pos
        if tree[pos] < key:
            pos = pos * 2 + 1
        else:
            pos = pos * 2
    return -1

lst = [9, 4, 12, 3, 6, 15, 13, 17]
tree = [0] * 100
for item in lst:
    insert(item)
    print(tree)

insert(5)
print(tree)
print(find(12))
print(find(9))