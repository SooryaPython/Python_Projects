""" 
Date: 20th April 2022
Name: S. Soorya
File description: String slicing
"""
# error will always be in the form of blank (or) empty line
d='python' # variable
print(d[:]) #python
print(d[1:]) #ython
print(d[2:]) #yhon
print(d[3:]) #hon
print(d[4:]) #on
print(d[5:]) #n
print(d[2:4]) #th
print(d[2:88]) #thon
print(d[-2:-6]) # Blank (or) empty line
print(d[0:1]+d[-5:-2]+d[4:]) # python
print(d[ : : ]) # python
print(d[1::2]) # yon
print(d[::2]) #pto skipping 2 times
print(d[::3]) #th skipping 3 times
print(d[::4]) #po skipping 4 times
print(d[1:4:5]) #y skipping 5 times from y to o
print(d[::-1]) # nohtyp skipping from backwards
q='department'
print(q[3]+q[2:]) # printing 'apartment' in 'department'
print(q[3:6]) # printing 'art' in 'department'

# Program finished.