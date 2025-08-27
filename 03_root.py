#Develop a program that receives a integer and calculates its square root.

number = input("Enter a number: ")
number = int(number)

root = number ** 0.5    #or number ** (1/2)
root = round(root, 4)
print("The square root of ", number, " is " , root)