""" 
Date: 24th May 2022
Name: S. Soorya
File description: Python MCQ based on Statements, Comments, and Indentation
"""
heading = "python quiz".title()
heading_center = heading.center(20)
by = "- soorya s".title()
by_center = by.center(30)
print(heading_center)
print(by_center)
Name = input("Enter your name to continue: ")
My_Name = Name
print("----------****----------")
print("Welcome" , My_Name)
print("""MCQ's based on Python programming language.
Rules and regulations to attend these MCQ's:
1) On each question, two options will be given. You need to just type the option's name but not the contents inside the option
and press enter.
3) If it is correct, then you will be getting a message as 'Correct answer!'.
4) If you type any wrong annswer, then the MCQ's will close automatically.
5) Try not to cheat this MCQ's.
6) Remember to be patient while attending the MCQ's.



""")
Continue = input("Do you want to continue? (1 for Yes, 0 for No): ")
if Continue == "1":
    print("Let's continue")
    print("""Question 1.
What is the output of the following program?
Program:
A = 90
 print(A)
a) IndentationError: unexpected indent
b) 90""")
    Answer_1 = input("Your answer: ").lower()
    if Answer_1 == "a":
        print("""Correct answer!
Question 2.
What is the output of the given program?
Program:
A = 11
B = 10
if A > b:
print("A is greater than B")
else:
    print("A is less than B") 
a) IndentationError: expected an indented block
b) NameError: name 'b' is not defined.
c) A is greater than B
d) IndentationError: unexpected indent""")
        Answer_2 = input("Your answer: ").lower()
        if Answer_2 == "a":
            print("""Correct answer!
Question 3:
Are comments mandatory or optional in Python?
a) Mandatory
b) There are no comments in Python.
c) Optional""")
            Answer_3 = input("Your answer: ").lower()
            if Answer_3 == "c":
                print("""Correct answer!
Question 4:
Which is used for single line and multiple line comments?
a) <!----> , //
b) // , #
c) # , ''''''
""")
                Answer_4 = input("Your answer: ").lower()
                if Answer_4 == "c":
                    print("""Correct answer!
BONUS:
Question 5.
Why Python 2.0 was estabilished?
a) Because HTML became popular among web developing.
b) Because Java was released at 1995.
c) C was used instead of Python
d) Because JavaScript was released at 1995.""")
                    Answer_5 = input("Your answer: ").lower()
                    if Answer_5 == "b":
                        print("""Correct answer!
Question 6.
What is the output of the following program?
Program:
print(''Hi.
Hello.'')
a) IndentationError: unexpected indent
b) Hi.
Hello.
c) SyntaxError: invalid syntax.
d) SyntaxError: unterminated string literal""")
                        Answer_6 = input("Your answer: ").lower()
                        if Answer_6 == "c":
                            print("""Correct answer!
Question 7.
What is the type of quote used to print a character?
a) Single ('') quotes
b) Both a and c
c) 3 single ('''''') quotes""")
                            Answer_7 = input("Your answer: ").lower()
                            if Answer_7 == "a":
                                print("""Correct answer!
Question 8.
What is the purpose of comments in all the programming and markup language?
a) The program will not execute when the comments are not there in a program.
b) For being understandable by the client or customer.
c) For being understandable by the database server.""")
                                Answer_8 = input("Your answer: ").lower()
                                if Answer_8 == "b":
                                    print("""Correct answer!
Question 9.
What is the name of joining or combining two or more strings joined by a '+' sign?
a) String combination
b) String addition
c) Quotation combination
d) String concadenation.""")
                                    Answer_9 = input("Your answer: ").lower()
                                    if Answer_9 == "d":
                                        print("""Correct answer!
Question 10.
How is a string represented?
a) print("str")
b) print('str')
c) Both a and b""")
                                        Answer_10 = input("Your answer: ").lower()
                                        if Answer_10 == "c":
                                            print("""Correct answer!
BONUS:
Question 11.
What is the full form of CMOS?
a) Complex Metallic Oxide Semiconductor.
b) Complimentary Metallic Oxidised Semiconductor.
c) Complimentary Metallic Oxide Systems.
d) Complimentary Metallic Oxide Semiconductor.""")
                                            Answer_11 = input("Your answer: ").lower()
                                            if Answer_11 == "d":
                                                print("Correct answer!")
                                                print("Congraluations" , My_Name + "!" , "You have completed the MCQ's.")
                                                print("""Hope you enjoyed!
            A MCQ's by Soorya S.
NO RIGHTS RESERVED.""")
                                        else:
                                            pass
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
else:
    print("Bye Bye!")