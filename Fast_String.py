""" 
Date: 6th May 2022
Name: S. Soorya
File description: About fast sting in Python
"""
# Fast string is to print variables in a shorter way.
""" NOTE: Variables must have a proper name """
sponser="Tata" # Variables
date_1="26th March 2022" # Variables
date_2="22nd May 2022" # Variables
year=2022 # Variables
print("IPL was sponsored by",sponser,"on the year",year,"scheduled from",\
date_1,"to",date_2) # 1st way to print this.
print("IPL was sponsored by "+sponser+" on the year "+str(year)+" scheduled \
from "+date_1+" to "+date_2) # Using string concadenation
print(f"IPL was sponsered by {sponser} on the year {year} scheduled from {date_1} \
to {date_2}") # Using fast string
""" 
About fast string:
* Used to make the print() statement easier to type
* {} --> Placeholder of the variable
* Shows "SyntaxError: f-string: empty experssion not allowed" when the placeholder is empty.
* Works only when "f" is present at the starting of the print() statement, like print(f{sponser}) \
where the sponser holds the value "Tata".
"""

# Program finished.