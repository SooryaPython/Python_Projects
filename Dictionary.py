""" 
Date: 19th May 2022
Name: S. Soorya
File description: About dictionary data type in Python
"""
# Dictionary is represented by {<KEYS>:<VALUE>}
dictionary_data_type = {1: "Pi thon"} # Variable
print(dictionary_data_type,type(dictionary_data_type)) # {1: 'Pi thon'} <class 'dict'>
# An empty set will also represent dictionary
empty_set = {} # Variable
print(empty_set,type(empty_set)) # {} <class 'dict'>
# As the name suggests, dictionary data type is used to make dictionaries
dictionary = {1: "Apple", 2: "Banana", 3: "Cat"}
# Printing keys
print(dictionary.keys()) # dict_keys({1, 2, 3})
# Printing values
print(dictionary.values()) # dict_values(['Apple', 'Banana', 'Cat'])
# To print the specified value
print(dictionary[1],type(dictionary[1])) # Apple <class 'str'>
print(dictionary[2],type(dictionary[2])) # Banana <class 'str'>
print(dictionary[3],type(dictionary[3])) # Cat <class 'str'>
# To find the dict methods
print(dir(dict)) # ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# clear() -> used to clear the elements in the dict. Output is {}
Trains = {1: "Train 18", 2: "LHB Rajdhani", 3: "ICF Coach"} # Variable
Trains.clear() # Clearing the values in Trains variable
print(Trains) # {}
# fromkeys() -> used to add the keys and values from the list
Coaches = {"LHB Rajdhani" , "LHB Duronto" , "ICF Garib Rath" , "ICF Blue" , "LHB Humsaffar"} # Variable
Numbers = {1, 2, 3, 4, 5} # Variable
print(dict.fromkeys(Numbers , Coaches)) # {1: {'LHB Rajdhani', 'ICF Blue', 'LHB Humsaffar', 'LHB Duronto', 'ICF Garib Rath'}, 2: {'LHB Rajdhani', 'ICF Blue', 'LHB Humsaffar', 'LHB Duronto', 'ICF Garib Rath'}, 3: {'LHB Rajdhani', 'ICF Blue', 'LHB Humsaffar', 'LHB Duronto', 'ICF Garib Rath'}, 4: {'LHB Rajdhani', 'ICF Blue', 'LHB Humsaffar', 'LHB Duronto', 'ICF Garib Rath'}, 5: {'LHB Rajdhani', 'ICF Blue', 'LHB Humsaffar', 'LHB Duronto', 'ICF Garib Rath'}}
# get() -> used to get only the value from the list by the keys
Vegetables = {1 : "Onion" , 2 : "Capsicum"} # Variable
print(Vegetables.get(1)) # Onion
print(Vegetables.get(2)) # Capsicum
print(Vegetables.get(253)) # None
# pop() -> used to pop or remove the specified item only. Unlike list where when the value of the pop is empty, the last one gets removed.
Editors = {10 : "Notepad" , 11 : "Notepad++" , 12 : "Microsoft Visual Studio Code"} # Variable
Editors.pop(11)
print(Editors) # {10: 'Notepad', 12: 'Microsoft Visual Studio Code'}
# Editors.pop(78.10)
# print(Editors) # KeyError: 78.1
# popitem() -> used to remove the last item from the dict
Unicode_References = {1 : "UTF-8" , 2 : "UTF-16" , 3 : "ASCII" , 4 : "UTF-8 DOM"} # Variable
Unicode_References.popitem()
print(Unicode_References) # {1: 'UTF-8', 2: 'UTF-16', 3: 'ASCII'}
# update() -> used to update items that is given
OS = {20 : "Android" , 21 : "Microsoft Windows" , 22 : "Linux"} # Variable
OS.update({20 : "Linux Kernel"}) # Updating 'Android' to 'Linux Kernel' under the key 20
OS.update({23 : "Mac OS"}) # Updating 'Mac OS' with key 23
print(OS) # {20: 'Linux Kernel', 21: 'Microsoft Windows', 22: 'Linux', 23: 'Mac OS'}
# setdefault() -> used to add a new key and value but not used to change the existing key and value in the dict
Bulbs = {100 : "Incadescent Bulb" , 101 : "Compact Flourescent Lamps"} # Variable
Bulbs.setdefault(102 , "Light Emmiting Diode") # Adding the key 102 and value 'Light Emmiting Diode' with it.
print(Bulbs) # {100: 'Incadescent Bulb', 101: 'Compact Flourescent Lamps', 102: 'Light Emmiting Diode'}

# Program Finished.