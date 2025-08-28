#Get an age and check if the person can drink

age = input("Enter your age, please: ")
age = int(age)
minimum_age = 18

if age >= minimum_age:
    print("You can drink!")
else:
    print("You cannot drink, go home or somewhere else!")