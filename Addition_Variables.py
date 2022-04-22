""" 
Date: 17th April 2022
Name: S. Soorya
File description: Addition of variables with respect to String, Float, Integer
"""
a=294 ; b=186 ; c=3.14159 ; d=7596.1488 ; e='Python' ; f="ORG"
"""These are variables where a, b, c, d, e, and f are variables; = is the operator: and 294, 186, 3.14159, 7596.1488, Python, and ORG are the values"""
print(a+b) # 294 + 186 = 480 . Integer + Integer = True.
print(b+c) # 186 + 3.14159 = 18914159 . Integer + Float = True.
print(c+d) # 3.14159 + 7596.1488 = 7599.29039 . Float + Float = True.
print(d+b) # 7596.1488 + 186 = 7782.1488 . Float + Integer = True.
print(f+e) # ORG + Python = ORGPython . String + String = True. The output will appear without any space between two diffrent variables.
# If you try String + Integer, String + Float, Float + String, Integer + String, the output will be an error, which is TypeError: can only concatenate str (not "int") to str

# Program finished.