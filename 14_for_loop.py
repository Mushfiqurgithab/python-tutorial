# Chapter - 14 for loop in python

'''
    for variable in sequence:
        statement
'''

#----------- Looping through a list using for loop

# my_friend = ["Ratul", "Rakib", "Rahin"]
# for friend in my_friend:
#     # for loop body
#     print(friend)

#----------- Looping through a string using for loop

# my_name = "Indranil"
# for string in my_name:
#     print(string)

#----------- the range() function

# for x in range(10):
#     print(x)
#       print("Hello world")

#----------- nested for loop

animal = ["tiger", "cat", "dog"]
sound = ["roars", "meow", "barks"]

for x in animal:
    # body of x for loop
    for y in sound:
        # body of nested y for loop
        print("The "+ x + " " + y)