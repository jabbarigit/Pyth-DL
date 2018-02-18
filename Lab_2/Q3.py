
"""Write a python program to create any one of the following management systems. You can also pick one of your own.

Prerequisites:
Your code should have atleast five classes.
Your code should have _init_ constructor in all the classes
Your code should show inheritance atleast once
Your code should have one super call Use of self is required Use at least one private data member in your code.
Use multiple Inheritance atleast once Create instances of all classes and show the relationship between them.
Your submission code should point out where all these things are present.
"""
################################################################################################
#####   a.Library Management System (should have classes for Person, Student, Librarian, Book etc.)
################################################################################################

from builtins import str

#########Classes are five

# First Class is Librarians
class librarians:
    def __init__(self, f_name, l_name, cat): #_init_ constructor
        self.first_name = f_name
        self.Last_name = l_name
        self.category = cat

# Second class is member
class members: # Class 1
    # Creating a constructor to initialize name, family, department
    def __init__(self, f_name, l_name, cat): #_init_ constructor
        self.first_name = f_name
        self.Last_name = l_name
        self.category = cat

# Third Class Students
class students:
    def __init__(self, f_name, l_name, cat): # _init_ constructor
        self.first_name = f_name
        self.Last_name = l_name
        self.category = cat

# 4th Class Books
class books(students, members, librarians):
    def __init__(self, auth, title, ed, area, f_name, l_name, cat): # _init_ constructor
        librarians.__init__(self, f_name, l_name, cat)
        students.__init__(self, f_name, l_name, cat) #_init_ constructor
        members.__init__(self, f_name, l_name, cat) # _init_ constructor
        self.title = title
        self.authors = auth
        self.edition = ed
        self.department = area

# 5th Class
#  Inheritance
class faculties(members):
    def __init__(self, f_name, l_name, cat, area): # _init_ constructor
        super().__init__(f_name, l_name, cat)# using super
        self.department = area

# Entering Librarian class
print("Entering a Librarian Details:")
LibrarianInfo = librarians("Khalid", "AlMalki", "HR")
print("first name : " + str(
    LibrarianInfo.first_name) + "\nlast name : " + str(LibrarianInfo.Last_name) + "\ndepartment: " + str(
    LibrarianInfo.category))

print("==========================================================")

# Adding a memeber Claas
print("Entering a memeber Details:")
MembersInfo = members("ABDOH", "Jabbari", "TCN")
print("first name: " + str(
    MembersInfo.first_name) + " \nlast name: " + str(
    MembersInfo.Last_name) + "\nDepartment: " + str(MembersInfo.category))

print("==========================================================")

# Entering a student Class
print("Entering a student Details: ")
StudentInfo = students("Gharib", "Gharibi", "Computer Science")
print("\nfirst name : " + str(
    StudentInfo.first_name) + "\nlast name : " + str(
    StudentInfo.Last_name) + "\nmajor : " + str(StudentInfo.category))

print("==========================================================")


# Entering book class
print(" Entering a Book Details:")
BookInfo = books("Behrouz A Forouzan", "Data Comunication and Networking", "5th"
                 ,"","", "","")
print("\nTitle : " + str(
    BookInfo.title) + "\nEdition: " + str(BookInfo.edition) + "\nauthors: " + str(BookInfo.authors))


print("==========================================================")

print("Entering a faculty Details")
FacultyInfo = faculties("Song", "Sejun", "ECE","")
print("\nfirst name : " + str(
    FacultyInfo.first_name) + "\nlast name : " + str(
    FacultyInfo.Last_name) + "\ndepartment : " + str(
    FacultyInfo.category))






