from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_age(cls, name, year):
        cls.year = year
        cls.name = name
        cls.age = datetime.today().year - cls.year + 1
        return Person(cls.name, cls.age)

    def check_age(self):
        if self.age > 19:
            return True
        else:
            return False
            





#Driver's code
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
