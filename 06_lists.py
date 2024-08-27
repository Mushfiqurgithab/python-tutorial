# Chapter - 06 Lists in python

# List is an ordered container
# Create a List
# pets = [] #empty list
# pets = ["Dog", "Cat", "Rabbit", "Horse"]
            # 0, 1, 2, 3 = Positive Indexing
            # -4, -3, -2, -1 = Negative Indexing
# print(pets)

# ----------- Indexing

# print(pets[0])  # access the first element
# print(pets[2])  # access the first element

# ----------- Negative Indexing

# print(pets[-3])

# ----------- Range of indexes

# print(pets[1:2])

# ----------- Adding Items to a list

# append()
# pets.append("Elephent")
# print(pets)

# insert()
# pets.insert(0,"Elephent")
# print(pets)

# ----------- Deleting item from a list

# pop()
# pets.pop()
# print(pets)

# remove()
# pets.remove("Cat")
# print(pets)

# ----------- Getting the length of a list

# print(len(pets))

# ----------- Changing an item value

# pets[1] = "Fish"
# print(pets)

# ----------- check if an item exists

# ----------- Membership Operator

# membership operator - in not in
# country = ["Bangladesh", "Australia", "Canada", "India"]
# check_item = "Australia" in country
# check_item = "Pakistan" not in country
# check_item = "Bangladesh" not in country
# print(check_item)

# country = ["Bangladesh", 2, 2.7, True]
# print(country)

# ----------- extending a list

# num1 = [1,2,3]
# num2 = [4,5,6]
# num1.extend(num2)
# print(num1)