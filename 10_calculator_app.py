# Chapter - 10 calculator app in python

#----------- 4th.function

def addition(num1, num2):
    result = num1 + num2
    print("{0}+{1}={2}".format(num1,num2,result))

def substraction(num1, num2):
    result = num1 - num2
    print("{0}-{1}={2}".format(num1,num2,result))

def multiplication(num1, num2):
    result = num1 * num2
    print("{0}*{1}={2}".format(num1,num2,result))

def division(num1, num2):
    if num2 == 0.0:
        print("Can't do divide by zero")
    else:
        result = num1 / num2
        print("{0}+{1}={2}".format(num1,num2,result))


while True:
#----------- 1st.display
    print("What do you want to do?")
    print("1 for addition")
    print("2 for substraction")
    print("3 for multiplication")
    print("4 for division")
    print("Enter Q or q To exit The Calculator")

#----------- 2nd.user input - 2 digit number

    choice = input("Enter Your Choice : ")
    if choice == 'Q' or choice == 'q':
        break
# taking 2 number as a input form user
    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))

#----------- 3rd.conditions

    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        substraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Invalid Choice")
