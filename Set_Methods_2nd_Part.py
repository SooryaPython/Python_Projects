""" 
Date: 18th May 2022
Name: S. Soorya
File description: About set methods in Python
"""
# isdigitjoint() -> x.isdigitjoint(y) - x set is checking whether any matching elements in the set are available on set y. 
isdigitjoint_set_variable_1={3.14159,"Is the digit joint?",None} # Variable 1
isdigitjoint_set_variable_2={None,5.14159,False} # Variable 2
isdigitjoint_set_variable_3=isdigitjoint_set_variable_1.isdisjoint(isdigitjoint_set_variable_2)
isdigitjoint_set_variable_4=isdigitjoint_set_variable_2.isdisjoint(isdigitjoint_set_variable_1)
print(isdigitjoint_set_variable_3) # False
print(isdigitjoint_set_variable_4) # False 
# issubset() -> x.issubset(y) - x is checking whether all the elements available in x is available in y
issubset_set_variable_1={1,2,3} # Variable 1
issubset_set_variable_2={1,2,3,4,5,6} # Variable 2
issubset_set_variable_3=issubset_set_variable_1.issubset(issubset_set_variable_2) 
issubset_set_variable_4=issubset_set_variable_2.issubset(issubset_set_variable_1)
print(issubset_set_variable_3) # True
print(issubset_set_variable_4) # False
# difference_update() -> x.difference_update(y) - the contents available in x and not available in y will be printed
difference_update_set_variable_1={3.14159,None,False} # Variable 1
difference_update_set_variable_2={False,45081,"None"} # Variable
difference_update_set_variable_3=difference_update_set_variable_1.difference_update(difference_update_set_variable_2)
difference_update_set_variable_4=difference_update_set_variable_2.difference_update(difference_update_set_variable_1)
print(difference_update_set_variable_3) # None
print(difference_update_set_variable_4) # None
# remove() -> used to remove the given items from the set
remove_set_variable={"Please remove me!",3.14159,None,"Don't remove me!"} # Variable
remove_set_variable.remove("Please remove me!") # Removing 'Please remove me!' from remove_set_variable Variable
print(remove_set_variable) # 'Please remove me!' will be removed
# When you try to remove something that is not given in the set, the output is KeyError: <THE GIVEN VALUE>
# symmetric_difference_update -> checking the difference form both the sets
symmetric_difference_update_set_variable_1={3.14159,"What is this?","PYTHON Prof.",True} # Variable 1
symmetric_difference_update_set_variable_2={3.14159,False,None,"None"} # Variable 2
symmetric_difference_update_set_variable_3=symmetric_difference_update_set_variable_1.symmetric_difference_update(symmetric_difference_update_set_variable_2)
symmetric_difference_update_set_variable_4=symmetric_difference_update_set_variable_2.symmetric_difference_update(symmetric_difference_update_set_variable_1)
print(symmetric_difference_update_set_variable_3) # None
print(symmetric_difference_update_set_variable_4) # None
# intersection_update() -> used to find the same characters available in both the sets
intersection_update_set_variable_1={3.14159,None,True,False} # Variable 1
intersection_update_set_variable_2={3.14159,"None","True",False} # Variable 2
intersection_update_set_variable_3=intersection_update_set_variable_1.intersection_update(intersection_update_set_variable_2)
intersection_update_set_variable_4=intersection_update_set_variable_2.intersection_update(intersection_update_set_variable_1)
print(intersection_update_set_variable_3) # None
print(intersection_update_set_variable_4) # NO\one

# Program finished