def enq(n):
    global last
    last += 1
    heap[last]= n
    c = last
    p = c // 2
    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

def deq(n):
    global last
    tmp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c+1 <= last and heap[c]