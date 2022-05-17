"""
Date: 16th May 2022
Name: S. Soorya
File description: About sets in Python
"""
# Set is a data type which is represented in curly brackets
set_data_type_variable={20} # Variable
print(set_data_type_variable,type(set_data_type_variable)) # {20} <class 'set'>
# Set when represented empty will turn into dictionary data type
dict_data_type_variable={} # Variable
print(dict_data_type_variable,type(dict_data_type_variable)) # {} <class 'dict'>
# Set when cleared will show the output as set
clear_set_variable={9} # Variable
clear_set_variable.clear()
print(clear_set_variable) # set()
# Set can hold many data types except list, set, dict and will always print the output in any order
set_data_type_holder_variable={12,3.14159,"All set!",True,False,None,(3.14159,"Tuple?",None)} # Variable
print(set_data_type_holder_variable,type(set_data_type_holder_variable)) # Will be printed in any order <class 'set'>
# To find the number of set methods
print(dir(set)) # ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
# Task: To practice the set methods
# add() -> used to add an element in the set
add_set_variable={90,"Addition",True} # Variable
add_set_variable.add("Please add me!") # Adding 'Please add me!' in the add_set_variable Variable
print(add_set_variable) # Will be printed in any order and will contain 'Please add me!' string
# clear() -> used to clear the characters available in the set. The output will be set()
clear_set_contents_variable={"Cls",74.10,98,True} # Variable
clear_set_contents_variable.clear() # Clearing the contents available in the clear_contents_set_variable Variable
print(clear_set_contents_variable) # set()
# difference() -> used to find the remaining contents only available in a set but not in the other set
set_difference_variable_1={90,None,"Sets!"} # Variable 1
set_difference_variable_2={89,None,"Tamarind"} # Variable 2
set_difference_variable_3=set_difference_variable_1.difference(set_difference_variable_2) # Finding the items that are not in set_difference_varaible_1 Variable but in set_difference_variable_2 Variable
print(set_difference_variable_3)
# difference_update() -> used to remove the items available in this set i.e. included in another, specified set
set_difference_update_variable_1={90,None,"Sets!"} # Variabe 1
set_difference_update_variable_2={89,None,"Tamarind"} # Variable 2
set_difference_update_variable_3=set_difference_update_variable_1.difference_update(set_difference_update_variable_2) # Idnetifying the items that is both available in set_difference_update_variable_1 Variable and set_difference_update_variable_2 Variable
print(set_difference_update_variable_3) # None
# discard() -> used to remove the specified item in the set
discard_set_variable={67,"Discard me!",3.14159,None} # Variable
discard_set_variable.discard("Discard me!") # Discarding 'Discard me!' from discard_set_varaiable Varaible
print(discard_set_variable) # {67, 3.14159, None}
# When you try to discard something that is not available in the set, the output will be the set itself
discard_set_none_variable={78,20.14159,"Dominion"}
discard_set_none_variable.discard("Error?")
print(discard_set_none_variable)

# Program not finished.