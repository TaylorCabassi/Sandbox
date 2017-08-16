"""Taylor"""
name = input("What is your name?: ")
for char in name:
    if char.isdigit():
        print("Invalid Name")
        name = input("What is your name?: ")
    if char.islower() ==0 or char.isupper() == 0:
        print("Invalid Name")
        name = input("What is your name?: ")
print(name[::2])
