""" 
Date: 9th June 2022
Name: S. Soorya
File description: About built in functions in Python
"""
"""BUILT-IN FUNCTIONS"""
"sort() or sorted()"
numbers = [59851 , 3694 , 10.055845 , 36315.2987 , -545]
numbers.sort()
print(numbers) # [-545, 10.055845, 3694, 36315.2987, 59851] # Descending order
numbers.sort(reverse = False)
print(numbers) # [-545, 10.055845, 3694, 36315.2987, 59851] # Descending order
numbers.sort(reverse = True)
print(numbers) # [59851, 36315.2987, 3694, 10.055845, -545] # Ascending order
"all()"
"Prints False when the given value is False, 0, empty string, None"
print(all([True, "Hi", 3.14159])) # True
print(all([False, "Hi", 3.14159])) # False
print(all([0, "Hi", 3.14159])) # False
print(all([None, "Hi", 3.14159])) # False
print(all(["", "Hi", 3.14159])) # False
print(all([False, 1, True])) # False
"any()"
"Prints True when the given value is True or 1. Else False"
print(all([True, "Hi", 3.14159])) # True
print(all([False, "Hi", 3.14159])) # False
print(all([0, "Hi", 3.14159])) # False
print(all([None, "Hi", 3.14159])) # False
print(all(["", "Hi", 3.14159])) # False
print(all([False, 1, True])) # False
"bool()"
print(bool(True)) # True
print(bool(False)) # False
print(bool(1)) # True
print(bool(0)) # False
print(bool("True?")) # True
print(bool("")) # False
"eval()"
eval_variable = eval(input("Enter any number: "))
print(f"The number you entered is {eval_variable}, which is", type(eval_variable))
"sum()"
addition = [4798465,4, 946154987, 546874654987465466,54, 676465479876458764,5468765465468786]
print(sum(addition)) # 1228808901280346526
"""FUNCTIONS: """
"A function:"
def my_function():
    print("Hello, World!")
my_function()
print("I am Soorya S.")
print("I love Python 3.10.4")