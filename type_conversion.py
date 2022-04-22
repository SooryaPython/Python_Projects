""" 
Date: 18th April 2022
Name: S. Soorya
File description: About the data type Boolean and adding the data types.
"""
# When multiplying String to String. Output will be: TypeError: can't multiply sequence by non-int of type 'str'
# The TypeError program while multiplying:print('holaman'*'hgijf')
"""The Boolean data type:
One bool data type is True: """
print(type(True)) # The output will be: <class 'bool'>
# Another bool data type is False
print(type(False)) # The output will be: <class 'bool'>
# Python is space sensitive.
"""When the program is:
 print("PyTHOnn")
The output will be: IndecationError: unexpected indent
"""
# When the program is:
print("PyTHOnn") # The output will be:PyTHOnn
#The len() starts to cound the letters of the sentence starting from 1. The program is: 
print(len("Queries")) # The answer will be: 7. Because Q is letter no. 1, U is letter no. 2, ......, s is letter no. 7. This
# Index starts the letter to count from 0. The program is:
a="Danny" # This is a variable where 'a' is the variable, '=' is the operator, 'Danny' is the value.
print(a[0]) # This prints the letter number 0 i.e. D
print(a[1]) # This prints the letter number 1 i.e. a
print(a[2]) # This prints the letter number 2 i.e. n
print(a[2]) # This prints the letter number 3 i.e. n
print(a[4]) # This prints the letter number 4 i.e. y
# isspace(): a Boolean where this recogonizes whether the program has space
print(' '.isspace()) # True
print(''.isspace()) # False
s='23.9320' # Value String
t=float(s)  # Value Float
print(int(t)) # To print string as integer.
print(str(t)) # To print float as string

# Program finished
