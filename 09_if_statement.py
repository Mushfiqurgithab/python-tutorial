# Chapter - 09 if statement in python

# x = 20
# y = 20
# # if statement
# if x<y:
#     # body of if
#     print("x is smaller than y")
# elif x>y:
#     # body of elif
#     print("x is greater then y")
# elif x==y:
#     print("x is equal")
# else:
#     # body of else part
#     print("enter right value")


# -----------  program to find out the user is eligiable for driving license or not

# user_age = int(input("Enter your age: "))
#
# if user_age>=18 and user_age<=45:
#     print("you are eligible for driving license")
# elif user_age>45 and user_age<=65:
#     print("your age is too high so change are not so good getting a driving license")
# else:
#     print("Sorry your age is to young")

# -----------  nested if statement

x = 13
if x<12:
    print("x is more then 5")
    # nested if-else
    if x>10:
        print("x is more then 10")
    else:
        print("x is not more then 5")
else:
    print("put right value")