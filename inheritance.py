# inheirtances,
class pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print('i dont know what to say')
    
    def show(self):
        print(f'i have a pet  named {self.name},it is {self.age} years old,')


class Cat(pet): # pet is the super class,passing pet here means i wouldnt need to re write the class pet code
                # for dog and cat
                # say i wanted to add another attribute to this class, i wont want to rewrite the code exactl again
                # i would need to refer to the super class pet and then add the attribute
    def __init__(self,name, age ,color):
         super().__init__(name,age)
         self.color = color

    def speak(self):
        print('meow')

    def show(self):
        print(f"i have a pet  named {self.name},it is {self.age} years old, it's am {self.color}")

class Dog(pet):
    def speak(self):
        print('bark')

class Fish(pet):
    pass

bingo =  Dog('bingo', 2)
bingo.speak()
b1 =  Cat  ("shii", 3, "Brown")
b1.show()
F1 = Fish('bubbles',2)
F1.speak()