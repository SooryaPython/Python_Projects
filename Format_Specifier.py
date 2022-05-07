""" 
Date: 6th May 2022
Name: S. Soorya
File description: Format specifiers in Python
"""
# Format specifier for integers --> %d and %i
integer_value_variable=20 # variable
# Printing 20 in many ways:
print(integer_value_variable) # 20
print(f"{integer_value_variable}") # 20
print('%d' %integer_value_variable) # 20
print('%i' %integer_value_variable) # 20
print('%d'                    %integer_value_variable) # 20
# Format specifier for float --> %f
float_value_variable=3.14 # variable
print(float_value_variable) # 3.14
print(f"{float_value_variable}") # 3.14
print("%f" %float_value_variable) # 3.140000
# The output of the above file is 3.140000 because the basic value of the float is 0.000000.
# In the place of 0.00 , 3.14 has occupied it.
# Format specifier for string --> %s
string_value_variable="Python" # Variable
# Printing Python in many ways:
print(string_value_variable) # Python
print(f"{string_value_variable}") # Python
print("%s" %string_value_variable) # Python

# Program Finished.