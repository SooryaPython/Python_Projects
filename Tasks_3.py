""" 
Date: 7th May 2022
Name: Soorya S
File description: About tasks in Python
"""
"Printing 1 to 10"
from cgi import print_form
from msilib.schema import CheckBox
from pathlib import PureWindowsPath


print("Numbers from 1 to 10:")
for i in range(1, 11) : print(i)
"Printing 100 to 110"
print("Numbers from 100 to 110:")
for i in range(100, 111) : print(i)
"Even or odd"
Number = int(input("Type any integer to check whether it is even or odd and press enter: ")) # Variable
if (Number % 2 == 0):
    print(f"The number {Number} is even.")
elif (Number % 2 != 0):
    print(f"The number {Number} is odd.")
else:
    print(f"The number {Number} is equal to zero.")
"evla"
Number_Eval = eval(input("Enter any one number and press enter: ")) # Variable
print(f"The number which you entered is {Number_Eval}, which is", type(Number_Eval))
"String letters"
str = input("Enter any one string and press enter: ") # Variable
print(f"The string which you entered is {str}")
print(f"The string {str} in reversed order is", str[::-1])
print(f"The string {str}, when skipped two times is", str[::2])
if str == str[::-1]: print(f"The string {str} is a palindrome.")
else: print(f"The string {str} is not a palindrome.")
"Display multiplication table"
Number = int(input("Enter any integer to find its multiplication table and press enter: ")) # Variable
for i in range(1, 13): print(Number, "X", i, "=", Number * i)
"Sum in list"
Number_1, Number_2, Number_3 = [float(x) for x in input("Type any three floats seperated by a space to find is sum: ").\
split()] # Variable
print("The sum is", Number_1 + Number_2 + Number_3)
"Check whether the item is in the list"
List = [x for x in input("Type many characters seperated by a space and press enter: ")] # Variable
Check_List = input("Type any character to check whether it is present on the previous list and press enter: ") # Variable
if Check_List in List: print(f"The character {Check_List} is in the list {List}")
else: print(f"The character {Check_List} is not in the list {List}.")
character = input("Type anything: ") 
if int(character) != ValueError: print(f"The number {character} can be converted into integer or string.")
else:  print(f"The number {character} cannot be converted into integer or string.")

# Program finished