""" 
Date: 27th May 2022
Name: S. Soorya
File description: About Number system in Python
"""
# For the use of decimals in Python
from decimal import Decimal as D
Decimal = D(0.7)
print(Decimal, type(Decimal)) # 0.6999999999999999555910790149937383830547332763671875 <class 'decimal.Decimal'> # Will print with long decimal digits
Long_Decimal_Sum = D(0.7+ 0.1)
print(Long_Decimal_Sum) # 0.79999999999999993338661852249060757458209991455078125
Short_Decimal_Sum = D(0.7)+ D(0.1) # Will give the exact half answer
print(Short_Decimal_Sum) # 0.7999999999999999611421941381
# To find the number of built-in functions in Python
print(dir(__builtins__)) # ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
# For the use of fractions:
from fractions import Fraction as F
Fraction = F(1, 2)
print(Fraction, type(Fraction)) # 1/2 <class 'fractions.Fraction'>
Simplify_Fraction = F(5, 10) # Will be simplified
print(Simplify_Fraction) # 1/2
# Zero = F(5, 0) # ZeroDivisionError: Fraction(5, 0)
# Zero_Fraction = F(5/ 0) # ZeroDivisionError: Fraction(5, 0)
""" Like we use comma in Mathematics to seperate the hunderds and thousands, we use underscoe(_) in Python.
This will neither change the value nor the data type of that particular character"""
Underscore = 98_76_54_321
print(Underscore, type(Underscore)) # 987654321, <class 'int'>
# isinstance() syntax() -> print(isinstance(variable, data-type))
Integer = 0
Float = 0.1
print(isinstance(Integer, int)) # True
print(isinstance(Float, float)) # True
print(isinstance(Float, int)) # False
print(isinstance(Integer, float)) # False
# Complex -> a data type used to represent in the formula b+ bj where b is real and bj is imaginary
Complex = 4+10j
print(Complex, type(Complex)) # (4+10j) <class 'complex'>
print(Complex.real) # 4.0 # In the format of float
print(Complex.imag) # 10.0 # In the format of float
# Ae0 -> A multiplied by 10 raised by the power of 0
print(1e0) # 1*10**0 = 1*1 = 1.0 # Always in float
print(10e2) # 10*10**2 = 10*100 = 1000
# The value of e in Python
import math as M
print(M.exp(1)) # 2.718281828459045 = e = 2.718281828459045
print(M.exp(10)) # 2.718281828459045*10 = 22026.465794806718
# print(M.exp(1000)) # OverflowError: math range error

# Program finished