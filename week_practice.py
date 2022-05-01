"""
Date: 1st May 2022
Name: S. Soorya
File description: For practice
"""
x = "abcdefghijklmnopqrstuvwxyz" # variable
print(x) # abcdefghijklmnopqrstuvwxyz
print(x[::-1]) # zyxwvutsrqponmlkjihgfedcba
print(x[0]+x[13]+" "+x[0]+x[15]+x[15]+x[11]+x[4]) # an apple
print(x[::2]) # skipping a to z two times
# Task 1: printing "a-b" in two different ways
print("a"+"-"+"b") # String concadenation
print("a","b",sep="-") # using ,sep= method
# Task 2: to print " hihello" in different ways
print("hihello")
print("hi"+"hello")
print("hi",end="")
print("hello")
# Some escape sequences
print("\alert") # alert escape sequence
print("\backspace") # backspace
print("\fnew line") # new line
# print("\xunicode") # unicode

# Program finished