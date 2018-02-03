''' user password validatation basic rules.
the following are the criteria for valid password:
a)	The password length should be in range 6-16 characters
b)	Should have atleast one number
c)	Should have one special character in [$@!*]'''

#########I will use loops to write codes for the above scenario.

import re  # IMPORT THE REGEX MODULE LIBRARY
password= input("Input your password !!make sure to read password rules!!:") # ENTER THE PASSWORD
x = True
while x:
    if (len(password)<= 6 | len(password)>= 16): # to check if the entered password length in the range of 6-16 characters.
        print("The password length should be in range 6-16 characters")
        break
    elif not re.search("[0-9]",password):
        print("the password MUST contain atleast one number")# to check if the entered password has numbers
        break
    elif not re.search("[$@!*]",password):
        print("your password MUST contain one special character")
        break
    elif not re.search("[a-z]", password):
        print(
            "your password must contain a lowercase letter")  # to check if the entered password has lowercase character
        break
    elif not re.search("[A-Z]", password):
        print(
            "your password must contain an upercase letter")  # to check if the entered password has uppercase character
        break
    else: # if the password passed all the above, issue the password
        print("the password you entered is valid")

        # if the passowrd is not meeting any of the requirements tell the user to try again then go out of the loop.

        x=False
        break
if x:
    print("please try to recreate your password again!!!")
