""" 
Date: 3rd June 2022
Name: Soorya S
File description: About errors and error handling in Python
"""
# To know about built-in functions in Python
print(dir(__builtins__))
# Some common errors in Python
"""ZeroDivisionError""" # a = 5 / 0 -> ZeroDivisionError: division by zero
"""NameError""" # print(error) -> NameError: name 'error' is not defined.
"""ValueError""" # string = "string" ; print(int(string)) -> ValueError: invalid literal for int() with base 10: 'string'
"""TypeError""" # string = "string" ; int = 1 ; float = 1.0 ; print(string + int + float) -> TypeError: can only concatenate str (not "int") to str
# Error handling
try:
    ZeroDivisionerror = 5/0
except:
    print("Zero blah blah blah")
#   Output: Zero blah blah blah
# or
try: # If in try block the content's output is ZerDivisionError, then it will print the contents in except block 
#                                                                                     or will print the contents in try block
    ZeroDivisionError = 5/0
except ZeroDivisionError:
    print("Zero blah blah blah")
#   Output: Zero blah blah blah
try:
    print(hh)
except:
    print("Not defined.")
finally:
    print("Response: YUP!")
#   Output: Not defined.
#           Response: YUP!
try:
    print("hh")
except:
    print("Not defined.")
finally:
    print("Response: YUP!")
#   Output: hh
#           Response: YUP!
# try:
#     print(5 / 0)
# except ValueError:
#     print("JoooJi")
#   Output: ZeroDivisionError
try:
    print(hh)
except:
    print("hh")
finally:
    print("Response: Huh?")
# Output: hh
#         Response: Huh?
try:
    print(KRK)
except NameError:
    print("KRK")
else:
    print("KRoo")
# Output: KRK
try:
    print("KRK")
except ValueError:
    print("KRKok")
else:
    print("KRoo")
# Output: KRK
#         Kroo

# Program FINISHED!!!!!!!!!!!!