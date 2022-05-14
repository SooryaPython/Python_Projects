"""
Date: 14th May 2022
Name: S. Soorya
File description: About tuple data types in Python
"""
# -> Variable having multiple values seperated by a comma or just a value with a comma is called tuple
tuple_variable_1=11, # Variable 1
tuple_variable_2="Hello",123 # Variable 2
print(tuple_variable_2,type(tuple_variable_2)) # ('Hello', 123) <class 'tuple'>
print(tuple_variable_1,type(tuple_variable_1)) # 11, <class 'tuple'>
# Tuple is immutable i.e. modifications can't be done
# immutable_tuple_variable="Dominion",1002 # Variable
# immutable_tuple_variable[0]="Happy?" # Editing immutable_tuple_variable Variable
# print(immutable_tuple_variable) # TypeError: 'tuple' object does not support item assignment
# Can't represent empty variable
# empty_tuple_variable=,
# print(empty_tuple_variable) # SyntaxError: invalid syntax
# Can hold several data types
several_data_types_tuple_variable=12,3.14159,"String",True,None,False,[72,90] 
print(several_data_types_tuple_variable,type(several_data_types_tuple_variable)) # (12, 3.14159, 'String', True, None, False, [72, 90]) <class 'tuple'>
print(several_data_types_tuple_variable[0],type(several_data_types_tuple_variable[0])) # 12 <class 'int'>
print(several_data_types_tuple_variable[1],type(several_data_types_tuple_variable[1])) # 3.14159 <class 'float'>
print(several_data_types_tuple_variable[2],type(several_data_types_tuple_variable[2])) # String <class 'str'>
print(several_data_types_tuple_variable[3],type(several_data_types_tuple_variable[3])) # True <class 'bool'>
print(several_data_types_tuple_variable[4],type(several_data_types_tuple_variable[4])) # None <class 'NoneType'>
print(several_data_types_tuple_variable[5],type(several_data_types_tuple_variable[5])) # False <class 'bool'>
print(several_data_types_tuple_variable[6],type(several_data_types_tuple_variable[6])) # [72, 90] <class 'list'>
# Can be printed seperatedly using index positions
index_position_tuple_variable=90,3.14159 # Variable
print(index_position_tuple_variable[0],type(index_position_tuple_variable[0])) # 90 <class 'int'>
print(index_position_tuple_variable[1],type(index_position_tuple_variable[1])) # 3.14159 <class 'float'>
# If you try to print an index position that is not available, the output will be IndexError: tuple index out of range
# print(index_position_tuple_variable[10000]) # IndexError: tuple index out of range
# Tuple methods: Count, Index
# count() -> Used to count the number of times the character is repeating in tuple
count_tuple_variable=90,None,"None",False,None # Variable
print(count_tuple_variable.count(None)) # 2
print(count_tuple_variable.count("None")) # 1
# When you try to count something whinch is not in the tuple, then the output is zero
print(count_tuple_variable.count(100000)) # 0
# index() -> used to find the index position given in the tuple
index_tuple_variable=3000,"Sonic The Hedgehog!" # Variable
print(index_tuple_variable.index(3000)) # 0
print(index_tuple_variable.index("Sonic The Hedgehog!")) # 1
# If you try to print any index position i.e. not in the tuple, the output will be ValueError: tuple.index(x): x not in the list
# print(index_tuple_variable.index("Sonic The Hedgehog")) # ValueError: tuple.index(x): x not in tuple
# To find the number of list methods 
print(dir(tuple)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# Program finished.