"""
Date: 30th May 2022
Name: S. Soorya
File description: Booking train tickets
"""
Heading = "train ticket bookings".title()
By = "- soorya s".title()
print(Heading, """
""")
print(By)
print("Log in to continue.")
Username = input("Username: ")
Password = input("Password: ")
print("Welcome", Username)
print("Train Ticket Bookings for Chennai Suburban Trains")
print("""Railway stations located between Chennai Beach - Chengalpattu route:
-------------------------------------------
Station number   Station name
--------------   ------------
0                Chennai Beach
1                Chennai Fort
2                Chennai Park
3                Chennai Egmore
4                Chetpet
5                Nungambakkam
6                Kodambakkam
7                Mambalam
8                Saidapet
9                Guindy
10               St Thomas Mount
11               Pallavanthangal
12               Meenambakkam
13               Tirusulam (Chennai International Airport)
14               Pallavaram
15               Chrompet
16               Tambaram Sanitorium
17               Tambaram
18               Perungalathur
19               Vandalur
20               Urapakkam
21               Guduvancheri
22               Potheri
23               Kattangalatur
24               Maraimalai Nagar
25               Kamarajar
26               Singaperumal Koil
27               Chengalpattu
-------------------------------------------

Type the station number only""")
From = int(input("From: "))
To = int(input("To: "))
if From > -1 and From < 28 and To > -1 and To < 28:
    print("Route: From station number", From, "to station number", To)
    Ph_No = int(input("Your Phone number: "))
    Verify = input("Enter your password to continue (Only 1 attempt): ")
    if Verify == Password:
        print("Rs. 20 will be transacted from the phone number", Ph_No, "**")
        print("By, Soorya S")
        print("NO RIGHTS RESERVED. ** This is just an practice.")
    else:
        print("Wrong password!")
else:
    print("Station number out of range.")