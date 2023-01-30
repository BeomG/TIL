class Calculator:
    def __init__(self,num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    
    def add(self):
        print(self.num_1 + self.num_2)

    def minus(self):
        print(self.num_1 - self.num_2)
    
    def multiply(self):
        print(self.num_1 * self.num_2)

    def division(self):
        if self.num_2 == 0:
            print('0으로 나눌 수 없습니다.')
        else:
            print(self.num_1 // self.num_2)
        

C1 = Calculator(1, 2)
C2 = Calculator(2, 1)
C3 = Calculator(3, 4)
C4 = Calculator(4, 0)

C1.add()
C2.minus()
C3.multiply()
C4.division()

# 1 + 2
# 2 – 1
# 3 * 4
# 4 / 0