""" 
Date: 17th May 2022
Name: S. Soorya
File description: About set methods in Python
"""
# intersection() -> used to find the same thing available in another given set
intersection_set_variable_1={3.14159,True,False,"False"} # Variable 1
intersection_set_variable_2={"False",102.14159,1234567890} # VAriable 2
intersection_set_variable_3=intersection_set_variable_1.intersection(intersection_set_variable_2) # Intersecting intersection_set_variable_1 Variable to intersection_set_variable_2 Variable
print(intersection_set_variable_3) # {'False'}
# union() and update() are used to combine two sets
union_and_update_set_variable_1={12,13,14} # Variable 1
union_and_update_set_variable_2={1,2,3,4,5,6,7,8,9,0} # Variable 2
union_and_update_set_variable_3=union_and_update_set_variable_1.union(union_and_update_set_variable_2) # Intersecting union_and_update_set_variable_1 Variable to union_and_update_set_variable_2 Variable
union_and_update_set_variable_4=union_and_update_set_variable_1.update(union_and_update_set_variable_2) # # Intersecting union_and_update_set_variable_1 Variable to union_and_update_set_variable_2 Variable
print(union_and_update_set_variable_4) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14}
# difference() -> used to find the items that are available in one set but not available in another specified sirt
difference_set_variable_1={12,13,14} # Variable 1
difference_set_variable_2={12,11,10} # Variable 2
difference_set_variable_3=difference_set_variable_1.difference(difference_set_variable_2) # Finding the difference between difference_set_variable_1 from difference_set_variable_2
difference_set_variable_4=difference_set_variable_2.difference(difference_set_variable_1) # Finding the difference between difference_set_variable_2 from difference_set_variable_1
print(difference_set_variable_3) # {13, 14}
print(difference_set_variable_4) # {10, 11}
# discard() -> used to discard the given item from the set
discard_set_variable={10,9,8,7} # Variable
discard_set_variable.discard(8)
print(discard_set_variable) # {9, 10, 7}
# When you try to remove items that is not in the set, then the output is None
print(discard_set_variable.discard("Error?")) # None
# pop() -> used to pop or remove any characters from the set randomly
pop_out_set_variable={"Will I be poped out?",3.14159,"Pi Thon",True} # Variable
pop_out_set_variable.pop()
print(pop_out_set_variable)

# Program finished