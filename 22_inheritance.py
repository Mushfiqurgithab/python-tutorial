# Chapter - 22 Advance /inheritance in python

'''
class Animal:
    def __init__(self,name):
        self.name = name
    def walk(self):
        print(self.name + " walks ")
a = Animal("Puppy")
a.walk()
'''

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print(self.name + " walks ")

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age )

    def sound(self):
        print(self.name + "barks")


x = Dog("Coco",1)
y = Dog("Alsa",1)
x.walk()
x.sound()
y.walk()
y.sound()