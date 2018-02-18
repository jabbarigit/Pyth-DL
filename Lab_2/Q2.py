list1={"Abdoh":['Abdoh','8189297373','jabbaria@umkc.edu'], "Khalid":['Khalid', '9132203333', 'ghep@umkc.edu']}

print('1. Display Contacts by Name')
print('2. Display Contacts by Number')
print('3. Edit Contacts by name')
print('4. To Quit')
Selection = input('what is your selection?')

if Selection == str(1):
    name1 = input('Enter a name to display its contact : ')
    for key in list1:
        if key == name1:
            print('Name   : ', list1[name1][0])
            print('Number : ', list1[name1][1])
            print('Email  : ', list1[name1][2])
elif Selection == str(2):
    num = input(' which number you want to display its contacts: ')
    for key in list1:
        if list1[key][1] == num:
            print('Name   : ', list1[key][0])
            print('Number : ', list1[key][1])
            print('Email  : ', list1[key][2])
elif Selection == str(3):
    name1 = input('Which name you need to edit it info: ')
    for key in list1:
        if key == name1:
            print("Eneter:", "\n n to edit number \n e to edit email")
            Option = input('your selection is : ')
            if Option == 'n':
                NewNumber = input('Insert the new number: ')
                list1[name1][1] = NewNumber
            elif Option == 'e':
                NewEmail = input('Add a new email: ')
                list1[name1][2] = NewEmail
            print('\nThe updated list of contact is: ')
            for key in list1:
                print('Name   : ', list1[key][0])
                print('Number : ', list1[key][1])
                print('Email  : ', list1[key][2])
                print('\n')
            pass

elif Selection == str(4):
    print('quiting')
    exit
else:
    print('Reselect again')