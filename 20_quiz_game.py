# Chapter - 20 quiz game in python

q1 ='''What is a correct syntax to output "Hello World" in Python?
a) echo("Hello World")
b) p("Hello World")
c) print("Hello World")
d) echo "Hello World"
'''
q2 ='''Which one is NOT a legal variable name?
a) my_var
b) my-var
c) _myvar
d) Myvar
'''
q3 ='''What is the correct file extension for Python files?
a) .pyth
b) .pt
c) .py
d) .pyt
'''
q4 ='''Which method can be used to return a string in upper case letters?
a) upper()
b) toUpperCase()
c) uppercase()
d) upperCase()
'''
q5 ='''Which operator is used to multiply numbers?
a) X
b) *
c) #
d) %
'''

# Create dicitionary
questions = {q1:"c", q2:"a", q3:"c", q4:"a", q5:"*"}
name = input("Enter your name: ")
print("Hello",name,"Welcome to the quiz")
score = 0
for i in questions:
    print(i)
    skip_question = input("Do you want to skip this question: please type (Yes/No)")
    if skip_question == "Yes" or skip_question == "yes":
        continue
    answer = input("Enter the correct answer (a/b/c/d): ")

    if answer == questions[i]:
        print("Correct Answer, You got 1 point")
        score = score + 1
        print("Current Score is :", score)
    else:
        print("Wrong answer, You lost 1 point")
        score = score - 1

    exit_quiz = input("Do you want to exit this quiz: please type (Yes/No)")
    if exit_quiz == "Yes" or exit_quiz == "yes":
        break

print("Final Score is",score)