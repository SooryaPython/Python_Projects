"""
Date: 7th May 2022
Name: S. Soorya
File description: About string methods in Python
"""
# upper() is used when we want to print the words in uppercase
print("python programmer".upper()) # PYTHON PROGRAMMER
print("PYTHON PROGRAMMER".upper()) # PYTHON PROGRAMMER
# isupper() is used to identify whether the words are uppercase(True) or not(False).
print("PYTHON PROGRAMMER".isupper()) # True
print("ptyhon programmer".isupper()) # False
print("Python Programmer".isupper()) # False
# lower() is used to print the words in lowercase
print("PYTHON PROGRAMMER".lower()) # python programmer
print("Python Programmer") # python programmer
# islower() is used to identify whether the words are lowercase(True) or not(False).
print("python programmer".islower()) # True
print("PYTHON PROGRAMMER".islower()) # False
print("Python Programmer".islower()) # False
# title() is ued to print each of the word's starting character in uppercase
print("string methods".title()) # String Methods
print("string Methods".title()) # String Methods
print("String Methods".title()) # String Methods
# istitle() is used to identify whether the words are in the format of title(True) or not(False).
print("String Methods".istitle()) # True
print("string Methods".istitle()) # False
print("String methods".istitle()) # False
print("string methods".istitle()) # False
# capitalize() is used to print the starting word's first character alone in uppercase manner
print("python programmer".capitalize()) # Python programmer
print("PYTHON PROGRAMMER".capitalize()) # Python programmer
print("Python Programmer".capitalize()) # Python programmer
# swapcase() is used to convert uppercase into lowercase and lowercase to uppercase
print("PythON".swapcase()) # pYTHon
print("pYTHON pROGRAMMER".swapcase()) # Python Programmer
# isalpha() is used to identify whether the print statements contains letters only(True) or not(False)
print("python".isalpha()) # True
print("PYTHON".isalpha()) # False
print("pyt hon".isalpha()) # False
print("pyt_hon".isalpha()) # False
print("pyt$hon".isalpha()) # False
# count() is used to count the number of times it is repeating
print("Python".count("P")) # 1
print("OhMamaMia".count("M")) # 2
print("OhMamaMia".count("m")) # 1
print("Python".count("f")) # 0
# find() is used to find the index position of the letter in the print statement. If there are no letters
# matching in the print statement, then the output will be -1
print("Questions".find("Q")) # 0
print("Questions".find("q")) # -1
print("Questions".find("s")) # 3
print("Questions".rfind("s")) # 8 # rfind() is used to find the 2nd same letter's index position in the print statement
# index() is used to find the index position in the print statement. If there are no letters matching 
# in the print statement, then the output will be ValueError: substring not found
print("Estimation".index("s")) # 1
# print("Estimation".index("y")) # ValueError: substring not found
print("Estimation".index("i")) # 3
print("Estimation".rindex("i")) # 7 # rindex() is used to find the 2nd same letter's index position in the print statement
# startswith() is used to identify whether the print statement is starting with the given letter(True) or not(False)
print("Hello".startswith("H")) # True
print("Hello".startswith("")) # True
print("Hi".startswith("h")) # False
print("Domination".startswith("Y")) # False
# endswith() is used to identify whether the print statement is ending with the given letter(True) or not(False)
print("Dominions".endswith("s")) # True
print("Dominions".endswith("")) # True
print("Dominions".endswith("f")) # False
# zfill() is used to fill the string statement with 0(Zeros)
print("What".zfill(2)) # What
print("What".zfill(3)) # What
print("What".zfill(4)) # What
print("What".zfill(5)) # 0What
print("What".zfill(6)) # 00What
print("What".zfill(7)) # 000What
# join() is used to join two string statements instead of ,sep= method
join_string_variable="H","e","l","l","o" # Variable
join_with_string_variable="_"
print(join_with_string_variable.join(join_string_variable)) # H_e_l_l_o
# print(join_string_variable.join(join_with_string_variable)) # AttributeError: 'tuple' object has no attribute 'join'
# None is a data type
none_data_type_variable=None
print(none_data_type_variable) # None
print(type(none_data_type_variable)) # <class 'NoneType'>
# Tuple is a data type which contains multiple values
tuple_integer_variable=1,2,3 # Variable
tuple_float_variable=1.0,1.1,1.2 # Variable
tuple_string_variable="A","P","P" # Variable
print(tuple_integer_variable) # (1,2,3) # Tuple is always enclosed in a bracket when printed.
print(tuple_float_variable) # (1.0,1.1,1.2)
print(tuple_string_variable) # ('A','P','P')
# Tuple with join()
tuple_string_join_variable="App" # Variable
tuple_with_string_join_variable="_" # Variable
print(tuple_with_string_join_variable.join(tuple_string_join_variable))
# print(tuple_string_join_variable.join(tuple_with_string_join_variable)) # AttributeError: 'tuple' object has no attribute 'join'
# strip() is used to remove spaces from right and left corner
strip_string_variable=" Python " # Variable
print(strip_string_variable) #  Python 
print(strip_string_variable.strip()) # Python
print(strip_string_variable.lstrip()) # Python # remove spaces from left corner
print(strip_string_variable.rstrip()) #  Python # remove spaces from right corner
# removeprefix() is used to remove the given characters from the first
remove_prefix_variable="Programmer" # Variable
print(remove_prefix_variable.removeprefix("r")) # Programme
print(remove_prefix_variable.removeprefix("mer")) # Program
print(remove_prefix_variable.removeprefix("Hi")) # Programmer
# removesuffix() is used tp rempve the given characters from the last
remove_suffix_variable="Domains" # Variable
print(remove_suffix_variable.removesuffix("s")) # Domain
print(remove_suffix_variable.removesuffix("ns")) # Domai
print(remove_suffix_variable.removesuffix("G")) # Domains
# String is immutable i.e. modification not allowed in Python
# replace() is used to replace the given print statement to the new given print statement
replace_string_variable="Programmer"
print(replace_string_variable.replace("Programmer","Python")) # Python

# Program Finished