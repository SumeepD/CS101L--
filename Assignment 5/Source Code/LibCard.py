libcard = input("What is your library card number?")
length = len(libcard)
if(length == 10):
    print("This card is valid!")
    if(libcard == '9999999999'):
        print("This card belongs to a student in School of computing and enginnering")
    else:
        print("This card belongs to a student in the School of Arts and Sciences")
while(length != 10):
    print("The card number needs to be 10 digits")
    libcard = input("What is your library card number?")
    length = len(libcard)
    if(libcard == '9999999999'):
        print("This card belongs to a student in School of computing and enginnering")
    else:
        print("This card belongs to a student in the School of Arts and Sciences")
