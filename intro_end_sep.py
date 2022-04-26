""" 
Date: 25th April 2022
Name: S. Soorya
File descripption: About ,sep= and ,end= method.
"""
# ,sep= is about seperating the commas in the print() statement, ONLY WORKS WHEN COMMAS ARE PRESENT IN THE print() STATEMENT
print('h''y') #hy
print('h'+'y') #hy
print('h ' 'y') #h y
print('h' ' y') #h y
print(1,2,3,4,5,6) #1 2 3 4 5 6
print(1,2,3,4,5,6,sep='-') #1-2-3-4-5-6
print(1,2,3,4,5,6,7,8,9,0,0,0,8,662,sep='@') # 1@2@3@4@5@6@7@8@9@0@0@0@8@662
print('PYTHon' 'we') #PYTHonwe
print('PYTHon'          'we') #PYTHonwe
print('PYTHon'+'we') #PYTHonwe
print('Q'  'R',sep=' ') # QR
print('Q' 'R',sep='#') #QR
print('Q','R',sep='#') # Q#RC
# print("python"+3+"version is"+"3.10.4") # TypeError: can only concatenate str (not "int") to str
print("python",3,"version is","3.10.4") # python 3 version is 3.10.4
print("python",3,"version is","3.10.4",sep="-") # python-3-version is-3.10.4
#,end= statement statement is about printing the next print() statement.
print('hello') # hello
print('bye') # bye
print("Helllo",end="") # HellloBYEEEEES
print("BYEEEEES")
print("Helllo",end="") # HellloBYEEEEES

print("BYEEEEES")
print("HOLA MIJO",end="  @") # HOLA MIJO  @HOLA MIGUEL
print("HOLA MIGUEL")

# Program finished.