"""
Date: 31st May 2022
Name: Soorya S
File description: Tasks on Python
"""
# Printing the name, id, and salary of the given values using input
Name = input("Enter your name: ") # Variable
ID = int(input("Enter your ID: ")) # Variable
Salary = float(input("Enter your salary: Rs.")) # Variable
print("Employee name:", Name, "Employee ID:", str(ID), "Employee's salary: Rs." + str(Salary))
# Finding the sum of the given values
Sum = [float(x) for x in input("Enter many float values seperated by a space and press enter: ")\
.split()]
print("The sum of", Sum, "is", sum(Sum))
# Finding the area of the circle
import math
Radius = float(input("Enter the radius of the circle to find its area: ")) # Variable
print("The area of the circle with the radius", Radius, "is", math.pi * Radius ** 2)
# Printing the first and last characters from the given character using input
Characters = input("Type any character and press enter: ") # Variable
print("The first character of the character", Characters, "is", Characters[0])
print("The last character of the character", Characters, "is", Characters[-1])
# Combining two string characters from the given character using input
Combination_Character_1, Combination_Character_2 = [str(x) for x in input("Enter any two characters seperated \
by a space and press enter: ").split()] # Variable
print("The combination of the character", Combination_Character_1, "and", Combination_Character_2, "is", \
Combination_Character_1 + Combination_Character_2)
# Finding the cube of the given number
Cube = float(input("Enter any one float value to find its cube: ")) # Variable
print("The cube of the given number", Cube, "solved using the ** method is", Cube ** 3)
print("The cube of the given number", Cube, "solved using the pow() method is", math.pow(Cube, 3))

# Program Finished