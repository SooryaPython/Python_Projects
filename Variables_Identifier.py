""" 
Date: 17th April 2022
Name: S. Soorya
File Description: About variable identifier using isidentifier()
"""
# The isidentifier() is about whether the variable name is applicable or not. THis is a Boolean function about 'True' or 'False'
print('w'.isidentifier()) # The output will be 'True' because the variable's name is starting with an alphabet.
print('3er'.isidentifier()) # The output will be 'False' because the variable's name is starting with a number.
print('_var63'.isidentifier()) # The output will be 'True' because the variable's name is starting with a underscore, middle is an alphabet, ending with an number.
print('ALL_Bj2'.isidentifier()) # The output will be 'True' because the variable's name is starting with an alphabet, middle is a underscore, ending with a number.

# Program finished.
