""" 
Date: 24th May 2022
Name: S. Soorya
File description: About types of operators in Python
"""
# Arithmetic operators:
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
print("The value of a + b is",a + b) # Addition
print("The value of a - b is",a - b) # Subraction 
print("The value of a * b is",a * b) # Multiplication
print("The value of a / b is",a / b) # Division
print("The value of a %" + " b is",a % b) # Modulus
print("The value of a ** b is",a ** b) # Power
# Floor division: used to prevent the float values that occurs when whe divide two int or float
FloorDivision = 5
FloorDivision1 = 2
print("The value of a / b is",a / b) # Normal division
print("The value of a // b is", a // b) # Floor division. NOTE: It prevents the output after the decimal point
# Assingment operator
Random_Variable = 60
Random_Variable_2 = -60
Random_Variable = Random_Variable + Random_Variable_2 # Reusing Random_Variable variable to add Random_Variable variable and Random_Variable_2 variable
print(Random_Variable) # 0
a = 5
a+= 4
print(a) # a = a+4 = 5+4 = 9
a = 5
a-= 4
print(a) # a =  a-4 = 5-4 = 1
a = 5
a*= 4
print(a) # a = a*4 = 5*4 = 20
a = 5
a/= 4
print(a) # a = a/4 = 5/4 = 1.25
# Relational or Comparision operators
# True for yes and False for no
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"The value of {a} > {b} is",a > b) # Greater than
print(f"The value of {a} < {b} is",a < b) # Lesser than
print(f"The value of {a} == {b} is",a == b) # As same as
print(f"The value of {a} != {b} is",a != b) # Not equal to
print(f"The value of {a} <= {b} is",a <= b) # Lesser than or equal to
print(f"The value of {a} >= {b} is",a >= b) # Greater than or equal to
# Relational or Comparisional operators using format specifier
# 0 for False and 1 for True
print("The value of a = %d , b = %d and a > b = %d" %(a,b,a > b)) # Greater than
print("The value of a = %d , b = %d and a < b = %d" %(a,b,a < b)) # Lesser than
print("The value of a = %d , b = %d and a == b = %d" %(a,b,a == b)) # Equal to
print("The value of a = %d , b = %d and a != b = %d" %(a,b,a != b)) # Not equal to
print("The value of a = %d , b = %d and a <= b = %d" %(a,b,a <= b)) # Lesser than or equal to
print("The value of a = %d , b = %d and a >= b = %d" %(a,b,a >= b)) # Greater than or equal to
# Logical operator: NOTE: Based on AND, OR, and NOT functions available on Truth Table
print("The value of a > b AND a < b is {}".format(a < b and a < b))
print("The value of a < b AND a < b is {}".format(a > b and a < b))
print("The value of a > b AND a < b is {}".format(a > b and a > b))
print("The value of a != b OR a != b is {}".format(a != b or a != b))
print("The value of a != b OR a == b is {}".format(a != b or a == b))
print("The value of a == b NOT a == b is {}".format(a, b, not  a == b))
print("The value of a == b NOT a != b is {}".format(a, b, not a != b))
# Bitwise operator: NOTE: Based on AND, OR, and NOT functions available on Truth Table
print("The value of a > b & a < b is {}".format(a < b & a < b))
print("The value of a < b & a < b is {}".format(a > b & a < b))
print("The value of a > b & a < b is {}".format(a > b & a > b))
print("The value of a != b | a != b is {}".format(a != b | a != b))
print("The value of a != b | a == b is {}".format(a != b | a == b))
print("The value of a == b ~ a == b is {}".format(a, b, ~ a == b))
print("The value of a == b ~ a != b is {}".format(a, b, ~ a != b))
# Identity operator
if a is b:
    print("a and b are same")
else:
    print("a and b are not same")
print("The identity of a",id(a))
print("The identity of b is",id(b))
print(type(a) is int)
print(type(b) is int)
# Membership operator
Names = ["Thalapathy Vijay" , "Dhanush" , "Superstar Rajnikanth" , "Robert Downey Jr."]
print("Robert Downey Jr." in Names) # True
print("Thalapathy Vijay" in Names) # True
print("Chris Pratt" in Names) # False
# Shift operator:
print(a << b) # Multiplying 2 times b to a
print(b << a) # Multiplying 2 times a to b
print(b >> a) # Dividing 2 times a to b
print(a >> b) # Dividing 2 times b to a

# Program finished