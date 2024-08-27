# Chapter - 05 working with string in python

# ----------- 1.single or double quotes

#hii i am mushfiq, i love "phyton" programming.
# text = 'Hii i am Mushfiq,I love "python" Programming'
# print(text)

# ----------- 2.Multi Line string

# text= '''Python is fun to learn,
# python is one of the easy language
# for sure you are having fun'''
# print(text)

# ----------- 3.Concatenating string (mean add or create connect with two string)

# a = "Hello "
# b = "World"
# text = a + b
# print(text)

# ----------- Accessing parts of a string ----------------------

# ----------- 1.indexing

# text = "I love python"
# print(text)
# # prints the 1st/I Character
# print(text[0])

# ----------- slicing

# text1 = "Python Lover"
# print(text1[2:5])  # text[start index : ending index]

# ----------- string methods -------------------

# ----------- 1.Capitalize string

name = "mushfiQ"
x = name.capitalize()
print(x)

# ----------- Convert to upper case

x = name.upper()
print(x)

# ----------- Convert to lower case

x = name.lower()
print(x)

# ----------- Get the Length of string
l = len(name)
print(l)

# ----------- Replaceing parts of string

text = "Hello World!"
print(text)
y = text.replace("World", "Everyone")
print(y)

# ----------- Check if a value is present in a string
