"""
Date: 11th May 2022
Name: S. Soorya
File description: About list methods in Python
"""
# append() -> will add only one element in the list
append_list_variable=[10,3.7,"Hello!"] # Variable
append_list_variable.append("Bye!") # Appending the append_list_variable Variable
print(append_list_variable) # [10, 3.7, 'Hello!', 'Bye!']
# If you try to add two elements in the list, then the output will be TypeError: list.append() takes exactly one argument (2 given)
# append_list_variable.append("Bye!","See you soon!") # Appending the append_list_variable Variable
# print(append_list_variable) # TypeError: list.append() takes exactly one argument (2 given)
# clear() -> used to clear the elements in the list
clear_list_variable=[99,2.345,"Decimal",None] # Variable
clear_list_variable.clear() # Clearing the clear_list_variable Variable
print(clear_list_variable) # []
# count() -> used to count the number of characters given in the brackets
count_list_variable=["Counting!",30,3.14159,True,True] # Variable
print(count_list_variable) # ['Counting!', 30, 3.14159, True]
print(count_list_variable.count(30)) # 1
print(count_list_variable.count(True)) # 2
print(count_list_variable.count(False)) # 0
# extend() -> used to add one or more characters in the list
extend_list_variable_1=[53.025,False,None] # Variable_1
extend_list_variable_2=[True,"True_False",102] # Variable_2
extend_list_variable_1.extend(extend_list_variable_2) # Extending extend_list_variable_1 Variable to extend_list_variable_2 Variable
print(extend_list_variable_1) # [53.025, False, None, True, 'True_False', 102]
# index() -> used to identify the index position in the list
index_list_variable=["Index",1,2,False,None] # Variable
print(index_list_variable.index("Index")) # 0
print(index_list_variable.index(None)) # 4
print(index_list_variable.index(1)) # 1
# If you try to find a index position that is not given in the list, then the output will be ValueError: <THE GIVEN VALUE> is not in the list
# print(index_list_variable.index("Error?")) # ValueError: 'Error?' is not in the list
# insert() -> used to add the contents in the given index position
insert_list_variable=[True,False,None] # Variable
insert_list_variable.insert(0,"Pi thon") # Inserting Pi thon in insert_list_variable Variable
print(insert_list_variable) # ['Pi thon', True, False, None]
insert_list_variable.insert(10000,None)
print(insert_list_variable) # ['Pi thon', 'Index', 1, 2, False, None, None]
# pop() -> used to show the last content in the list
pop_list_variable=[True,None,"Pop"] # Variable
print(pop_list_variable.pop()) # Pop
# Can also be used to pop content in the list using index position
print(pop_list_variable.pop(1)) # None
# If you try to pop an index that is not available in the list, then the output will be IndexError: pop index out of range.
# print(pop_list_variable.pop(10)) # IndexError: pop index out of range
# remove() -> used to remove the content given in the brackets
remove_list_variable=[True,"String",None] # Variable
remove_list_variable.remove("String")
print(remove_list_variable) # [True, None]
# If you try to remove a character that is not given in the list, then the output will be ValueError: list.remove(x): x not in the list
# remove_list_variable.remove("Error?")
# print(remove_list_variable) # ValueError: list.remove(x): x not in list
# reverse() -> used to reverse the order. Default value->True(ascending order)
reverse_list_variable=[78,65,14,20,30] # Variable
reverse_list_variable.reverse()
print(reverse_list_variable) # [30, 20, 14, 65, 78]

# Program finished