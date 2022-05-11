""" 
Date: 11th May 2022
Name: S. Soorya
File description: About list in Python
"""
""" 
List:
* Represented in square[] brackets
* Contains several data types: int, str, float, None, bool
* List is mutable i.e. modifications can be done in Python
"""
list_variable=[] # Variable containing list data type
print(list_variable,type(list_variable)) # [] <class 'list'>
# Printing the data types insude the lists
list_data_type_variable=["Dominion",10,3.14159,None,True,False] # Variable containing many data type in list data type
print(list_data_type_variable,type(list_data_type_variable)) #['Dominion', 10, 3.14159, None, True, False] <class 'list'>
print(list_data_type_variable[0],type(list_data_type_variable[0])) # Dominion <class 'str'> 
print(list_data_type_variable[1],type(list_data_type_variable[1])) # 10 <class 'int'>
print(list_data_type_variable[2],type(list_data_type_variable[2])) # 3.14159 <class 'float'> 
print(list_data_type_variable[3],type(list_data_type_variable[3])) # None <class 'NoneType'>
print(list_data_type_variable[4],type(list_data_type_variable[4])) # True <class 'bool'>
print(list_data_type_variable[5],type(list_data_type_variable[5])) # False <class 'bool'>
# Modifying the lists
modifying_list_variable=[1,3.10,"Array"] # Variable containing list data type
modifying_list_variable[0]=1000 # modifying 10 to 1000
modifying_list_variable[2]="Gorrila" # modifying 'array' to 'gorrila'
print(modifying_list_variable) # [1000, 3.1, 'Gorrila']
# There can be a list inside a list
list_inside_list_variable=["Horray!",2022,[11,0.5]] # Variable containing list inside a list
print(list_inside_list_variable[2][0],type(list_inside_list_variable[2][0])) # 11 <class 'int'>
print(list_inside_list_variable[2][1],type(list_inside_list_variable[2][1])) # 0.5 <class 'float'>
# To check the number of string methods:
print(dir(str)) # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# To check the number of list methods:
print(dir(list)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Program Finished.