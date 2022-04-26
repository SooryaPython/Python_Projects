"""
Date: 26th April 2022
Name: S. Soorya
File description: About ,sep= and ,end= method in the print() statement
"""
# Printing h e l l o in many ways:
print("h","e","l","l","o") # h e l l o
print('h','e','l','l','o') # h e l l o
print("h"+" "+"e"+" "+"l"+" "+"l"+" "+"o") # h e l l o (using string concadenation)
# Printing p@y in diffrent ways:
print("p"+"@"+"y") # p@y (using string concadenation)
print("p","y",sep="@") # Separeting p and y with @ using ,sep= method
# Printing hi through ,end= method:
print("h",end="")
print("i") # Output: hi
print("h",end="&+_%")
print("i") # Output: h&+_%i
# Printing "p-3.10.4 verion" in two ways:
print("p"+"-"+"3.10.4"+" version") # p-3.10.4 version
print("p","3.10.4",sep="-",end=" version") # p-3.10.4 version
# Task: To print "He'll"o" in four different ways:
print('He\'ll"o')
print("He'll\"o")
print("""He'll"o""")
print('''He'll"o''')

# Program finished.