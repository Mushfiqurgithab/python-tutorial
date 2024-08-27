# Chapter - 19 Advance /class & object in python

'''
# part 1

# create Class
class person:
    # body of person class
    # class properties
    first_name = "Mushfiq"
    last_name = "Rahman"
    age = 23
person_obj = person() # class object
# access properties
firstName = person_obj.first_name
lastName = person_obj.last_name
age = person_obj.age
# print the values of person class
print("First Name : ", firstName)
print("Last Name : ", lastName)
print("Age : ", age)

'''

'''
part -2

# class with attribute
# creating an instance of the class
class student:
    def __init__(self,id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age

student1 = student(123, "Rocky",21) # instance
student2 = student(124, "Dev", 22)
x = student1.id_number
y = student1.name
z = student1.age

print("Student 1 roll no is: ", x)
print("Student 1 name no is: ", y)
print("Student 1 age no is: ", z)
# instance are always unique

print("Student 2 roll no is: ", student2.id_number)
print("Student 2 name no is: ", student2.name)
print("Student 2 age no is: ", student2.age)
'''

# class with attribute
# creating an instance of the class
class student:
    def __init__(self,id_number, name, age):
        self.id_number = id_number
        self.name = name
        self.age = age
    def greet_student(self):
        print("Hello " + self.name + ", How are you?")

student1 = student(123, "Rocky",21) # instance
student2 = student(124, "Dev", 22)
student3 = student(125, "Rahim", 23)
student3.greet_student()
x = student1.id_number
y = student1.name
z = student1.age

print("Student 1 roll no is: ", x)
print("Student 1 name no is: ", y)
print("Student 1 age no is: ", z)
# instance are always unique

print("Student 2 roll no is: ", student2.id_number)
print("Student 2 name no is: ", student2.name)
print("Student 2 age no is: ", student2.age)

print("Student 3 roll no is: ", student3.id_number)
print("Student 3 name no is: ", student3.name)
print("Student 3 age no is: ", student3.age)