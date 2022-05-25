""" 
Date: 21st May 2022
Name: S. Soorya
File description: About for loop and inputs in Python
"""
# An simple addition program:
addent_1 = float(input("Enter the first addend and click enter:"))
addent_2 = float(input("Enter the second addend and click enter:"))
print("The sum is",addent_1 + addent_2)
# An addition program based on for loop
addent1,addent2=[float(x) for x in input("Enter the first and second addend seperated by a comma and click enter:").split(",")]
print("The sum is",addent1+addent2)
# An subtraction program based on for loop
addent1,addent2=[float(x) for x in input("Enter the first and second subrahend seperated by a comma and click enter:").split(",")]
print("The difference is",addent1-addent2)
# A simple multiplication program on for loop
import math
multiplication=[float(x) for x in input("Enter the multiplicand and multiplier seperated by a comma and press enter:").split(",")]
print(math.prod(multiplication))
# Factorial
print("NOTE: Accepts only integers, positive numbers for factorization.")
import math
factorial=[int(x) for x in input("Enter any number to find the factorial of it and press enter:")]
print(math.factorial(factorial))