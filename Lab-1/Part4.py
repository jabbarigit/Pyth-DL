
""" Consider the following scenario. You have a list of students who are attending
class “Python” and another list of students who are attending class “Web Application”.
****find the list of students who are attending both the classes.
Also find the list of students who are not common in both the classes."""

# the list of Python and Web application classes students
Python_students = ["Abdoh", "Tajul", "Mamon", "Rahfidah","Helen", "Mark", "Khalid"]
Web_Application_students = ["Abdoh", "Tajul", "Mamon", "Moo", "Rahfidah", "Sarah","Helen", "Harry"]

#start the loop to check on the two classes' lists to find the common names
for x in Python_students:
    for y in Web_Application_students:
        if x == y:
            print(x + ' is in both classes')

# now here start the second check to find the list of names not attending both classes.
c=0 # start from the bigenning
print("Below are the list of students who are not common in both the classes")# this line seprate between the two lists
for x in Python_students:
    for y in Web_Application_students:
        if x == y:
            c=1
    if c==1:
        c=0
    elif c==0:
        print(x)
