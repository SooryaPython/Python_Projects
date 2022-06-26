"""
Date: 26th May 2022
Name: Soorya
File description: Python
"""
# Filter:
def even(x):
        if x % 2 == 0:
                return True
        else:
                return False
x = [int(x) for x in input("Type many numbers seperated by a space: ").split()]
y = list(filter(even , x))
print(f"From {x} the even numbers are: {y}")
# Return:
def Sum(a,b):
        c = a + b
        return c
# Sum:
x = int(input("Enter any one number: "))
y = int(input("Enter another number: "))
z = x , y
print(f"The sum of {x} and {y} is" , sum(z))
# Lambda:
x , y = [int(x) for x in input("Enter any two numbers: ").split()]
Lambda = lambda x , y : x if x > y else y
print(f"The greatest numbers among {x} and {y} is" , Lambda(x , y))
# Lambda :
list_1 = [int(x) for x in input("Enter many numbers seperated by a space: ").split()]
list_2 = list(map(lambda x: x**2 , list_1))
print(f"The squares of the numbers {list_1} is" , *list_2)
# lambda with reduce
from functools import * # Reduce's module
list = [int(x) for x in input("Enter many  numbers seperated by a space: ").split()]
Addition = reduce(lambda x , y : x + y , list)
Subtraction = reduce(lambda x , y : x - y , list)
print(f"The sum of {list} is {Addition}")
print(f"The difference of {list} is {Subtraction}")
# Positional argument: 
def my_function(content_1 , content_2):
        content_3 = content_1 + content_2
        print(f"The sum of {content_1} and {content_2} is {content_3}")
my_function(0 , 1)
content_1 , content_2 = [int(x) for x in input("Enter any two numbers").split()]
# Local and global:
c = 200 # Global variable
def my__function():
        c = 20 # local variable
        print(c) # Will print from the local variable as it is inside the function
print(c) # Will print from the global variable as local can be acessed inside a function only.
my__function()
print(c) # # Will print from the global variable as local can be acessed inside a function only.
# Converting local to global
c = 200 # Global variable
def global_variable():
        global c
        c = 20
        print(c) # 20
print(c) # Prints from the global variable
global_variable()
print(c) # Prints from the local variable converted into global variable when the function is called
# Class
class my_class(): # A class
        variable = "Python 3.10.5" # Attribute
        
        def Class():
                print("I'm a function 'Class' inside a class 'my_class' dude!")
# Printing the functions
print(my_class.variable)
print(my_class.Class())
variable = my_class()
print(variable.variable)
print(variable.Class())
"""Inheritances: """ 
""" parent class """
class Animal:
    livingthing=True
    
    def eat():
        print("eating")
        
    def sleep():
        print("sleep")

# """child class"""
class goat(Animal):
    
    def grass():
        print("Its eating grass")
        
    def herb():
        print("It is herbivorus")

    def sleep():
        print("Don't sleep you are 820Rs Kg")

print(goat.livingthing)  # child class and accessing the parent class variable
print(Animal.livingthing)  # parent class and accesing class variable
goat.grass()
goat.herb()
goat.eat()
goat.sleep()
Animal.eat()
Animal.sleep()
Animal.herb()

""" Part-2 Calling with the help of an object"""
class Animal:
    livingthing=True
    
    def eat(self):
        print("eating")
        
    def sleep(self):
        print("sleep")

"""child class"""
class goat(Animal):
    
    def grass(self):
        print("Its eating grass")
        
    def herb(self):
        print("It is herbivorus")

    def sleep(self):
        print("Don't sleep you are 710Rs Kg")

a=Animal()
print(a.livingthing)
a.eat()
a.sleep()

g=goat()
g.grass()
g.herb()
g.sleep()
print(g.livingthing)
g.eat()
