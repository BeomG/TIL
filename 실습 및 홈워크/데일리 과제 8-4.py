class Stack:
    def __init__(self, lst):
        self.lst = lst
        self.lst = []

    def empty(self):
        if len(self.lst) == 0:
            print(True)
        else:
            print(False)
    
    def top(self):
        print(self.lst[-1])

    def pop(self):
        try:
            print(self.lst.pop())
        except:
            print(None)

    def push(self,A):
        self.lst.append(A)
        
    def __reper__(self):
        print(self.lst)


a = Stack('a')
a.empty()
a.__reper__()
a.pop()
a.push('D')
a.__reper__()
a.pop()