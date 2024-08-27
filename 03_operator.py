# Chapter - 03 operator in python
# Type of Operator
# -----Arithmetic Operator

# print(10+20) # addition
# print(10-20) # subtraction
# print(10*20) # multipilication
# print(12/5) # division
# print(10**2) # exponentitation
# print(10%20) # remainder
# print(12//5) # floor division

# -----Assignment Operator

x = 4
y = 3
x += y # x = x + y
print(x)

# -----Comparison Operator true or false

x = 10
y = 20
compare = x >= y #greater then
# compare = x<y #less then
# compare = x==y #equality
# compare = x!=y #not equality
print(compare)

# -----Logical Operator ture false and or not

# ...Logical "and" operator
# True table
# TT = True
# TF = False
# FT = False
# FF = False

x = 15
y = 25
logical_and  = x>y and x==y
# false and false
# Output - false
print(logical_and)

x = 35
y = 25
logical_and  = x>y and x<y
# true and true
# Output - true
print(logical_and)

# ...Logical "or" operator
# True table
# TT = True
# TF = True
# FT = True
# FF = False

x = 15
y = 25
logical_and  = x>y or x<y
# false and false
# Output - false
print(logical_and)

# ...Logical "not" operator

x = 15
y = 25
logical_and  = not x>y
# not false
# output - true
print(logical_and)

# -----Indentity Operator
# -----Membership Operator