"""
Date: 1st June 2022
Name: Soorya S
File description: Tasks on Python
"""
# To find whether the number is even or odd
Number = int(input("Type any integer to check whether it is even or odd: ")) # Variable
if Number % 2 == 0:
    print(f"The number {Number} is even.")
else:
    print(f"The number {Number} is odd.")
# To find whether the character is a palindrome or not
Palindrome = input("Type any character to check whether the character is a palindrome: ").lower() # Variable
if Palindrome == Palindrome[::-1]:
    print(f"The character {Palindrome} is a palindrome.")
else:
    print(f"The character {Palindrome} is not a palindrome")
# To find whether the integer is prime or composite.
Number = int(input("Enter any integer to check whether it is prime or composite: ")) # Variable
Flag = False # A flag value
if Number > 1:
    for i in range(2, Number):
        if (Number % i) == 0:
            Flag = True
            break
if Flag:
    print(f"The number {Number} is a composite number.")
else:
    print(f"The number {Number} is a prime number.")
# Leap year or non-leap year program
Year = int(input("Enter any one year to check whether it is leap year or non-leap year: AD ")) # Variable
if Year % 4 == 0:
    print(f"The year {Year} is a leap year.")
else:
    print(f"The year {Year} is a non-leap year.")
# To check whether the number is positive, negeative, or zero
Number = float(input("Enter any number to check whether the number is positive, negeative, or zero: ")) # Variable
if Number > 0:
    print(f"The number {Number} is a positive number.")
elif Number < 0:
    print(f"The number {Number} is a negeative number.")
else:
    print(f"The number {Number} is equal to zero.")
# Largest among three numbers
Number_1, Number_2, Number_3 = [float(x) for x in input("Enter any three float values seperated \
by a space to check which one is the greatest: ").split()] # Variable
if Number_1 > Number_2 and Number_1 > Number_3:
    print(f"The number {Number_1} is the greatest when compared with {Number_2} and {Number_3}.")
elif Number_2 > Number_1 and Number_2 > Number_3:
    print(f"The number {Number_2} is the greatest when compared with {Number_1} and {Number_3}.")
elif Number_1 == Number_2 == Number_3:
    print(f"The numbers {Number_1}, {Number_2}, and {Number_3} is equal to each other.")
elif Number_3 > Number_1 and Number_3 > Number_2:
    print(f"The number {Number_3} is the greatest when compared with {Number_2} and {Number_1}.")
# Fibonacci sequence:
Number = int(input("Enter the terms of fibonacci sequence: ")) # Variable
# First two terms:
Number_1, Number_2 = 0, 1
Count = 0
# check if the number of terms is valid
if Number <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif Number == 1:
   print("Fibonacci sequence upto", Number,":")
   print(Number_1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while Count < Number:
       print(Number_1)
       nth = Number_1 + Number_2
       # update values
       Number_1 = Number_2
       Number_2 = nth
       Count += 1

# Program finished