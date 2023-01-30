class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0 
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self,name):
        print(f'{name}: bark')
    
    def __del__(self):
        Doggy.num_of_dogs -= 1

    @classmethod
    def get_status(cls):
        print(Doggy.num_of_dogs, Doggy.birth_of_dogs)