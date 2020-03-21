ages = {}
for i in range(3):
    name = input("Name: ")
    age = int(input("Age: "))
    ages[name] = age

print(ages)

name = input("What is your name? ")
age = ages[name]
print(f"{name} - you are {age} years old")