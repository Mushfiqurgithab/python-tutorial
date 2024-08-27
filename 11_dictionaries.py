# Chapter - 11 dictionary in python

'''dictionary_name = {
    key:value,
    key:value,
}'''

#----------- creating a dictionary

# person = {
#     "first_name": "john",
#     "last_name": "Doe",
#     "age": 30
# }
# print(type(person))

#----------- accessing item

# x = person["first_name"] # dictinary[key]
# y = person["last_name"]
# z = person["age"]
# print("First Name: ",x)
# print("Last Name: ",y)
# print("Age: ",z)

#----------- get() method

# get_method = person.get("first_name")
# print(get_method)

#----------- adding new items

# person["hobby"] = "Playing cricket"
# print(person)

#----------- changing on item's value

# person["first_name"] = "Indranil"
# print(person)

#----------- removing an item value

# pop() method
# person.pop("age")
# print(person)
#----------- nested dictionary

employee_data = {
    # nestted dictionary
    "manager":{
        "name":"Mushfiq",
        "age":20
    },
    "programmer":{
        "name":"Rahman",
        "age":25
    },
    "salary":{
        "manager_salary":45000,
        "programmer_salary":39000
    }
}

# print manager name and age and salary
print("Manager name is:", employee_data["manager"]["name"],
      "\nmanager age is: ",employee_data["manager"]["age"],
      "\nmanger salary is: ",employee_data["salary"]["manager_salary"],
      )

# print programmer name and age and salary

print("Programmer name is:", employee_data["programmer"]["name"],
      "\nProgrammer age is: ",employee_data["programmer"]["age"],
      "\nProgrammer salary is: ",employee_data["salary"]["programmer_salary"],
      )
