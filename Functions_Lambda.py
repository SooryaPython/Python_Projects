""" 
Date: 11th May 2022
Name: Soorya S
File description: Functions and Lambda in Python
"""
"A Function - 1"
def normal_function(): # Introducing the function - normal_function
    print("Hello, World!")
    # Contents inside normal_function function
normal_function() # Calling the function
"Part 2:"
def function(parameter):
    print(f"Hi, {parameter}")
function("the value in the parameter 'parameter' : blah blah blah")
"Part 3:"
def function(variable):
    print(f"Hi, {variable}")
function("Python 3.10.4")
function("HTML 5.2")
"Part 4:"
def specification(*specify_me):
    print("Hello,", specify_me[0][0])
    print("Hello,", specify_me[0][1])
    print("Hello,", specify_me[0][2])
specification(("Python 3.10.4" , "HTML 5.2" , "PHP 7.0")) # Tuple
"Part 5:"
def specification(*specify_me):
    print("Hello,", specify_me[0][0])
    print("Hello,", specify_me[0][1])
    print("Hello,", specify_me[0][2])
specification(["Python 3.10.4" , "HTML 5.2" , "PHP 7.0"]) # List
"Part 6:"
def information(x , y):
    print(x , y)
information(x = True , y = False)
"Doc - Strings"
def doc_strings():
    """Hello! I'm a doc-string in Python!"""
print(doc_strings.__doc__)
"Lambda"
x = lambda: a + b + c
y = lambda: a - b - c
z = lambda: a * b * c
k = lambda: a / b / c
a , b , c = [float(x) for x in input("Enter any three numbers seperated by a space and press enter: ").split()]
print(f"The sum of {a}, {b}, {c} is {x}")
print(f"The difference of {a}, {b}, {c} is {y}")
print(f"The product of {a}, {b}, {c} is {z}")
print(f"The quotient of {a}, {b}, {c} is {k}")
"EVEN OR ODD?"
def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is EVEN!")
    else:
        print(f"{number} is ODD!")
even_or_odd(int(input("Enter any one integer: ")))
"LEAP YEAR OR NON_LEAP YEAR?"
def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is a LEAP YEAR!")
    else:
        print(f"{number} is a NON LEAP YEAR!")
even_or_odd(int(input("Enter any one year: ")))

# Program FINISHED