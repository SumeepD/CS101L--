print("            Grade Menu\n")
print("1 - Add Test")
print("2 -Remove Test")
print("3 -Clear Tests")
print("4 -Add Assignment")
print("5 -Remove Assignment")
print("6 -Clear Assignments")
print("D -Display Scores")
print("Q -Quit")
num = input()
while(num != 'Q'):
    if(num == '1'):
        add = int(input("What test score would you like to add?"))
    elif(num == '2'):
        add = int(input("What test score would you like to remove?"))
    elif(num == '3'):
        add = int(input("How many tests would you like to clear?"))
    elif(num == '4'):
        add = int(input("what assignment score would you like to add?"))
    elif(num == '5'):
        add = int(input("What assignment score would you like to remove?"))
    elif(num == '6'):
        add = int(input("How many assignments would you like to clear?"))
    elif(num == 'D'):
        add = int(input("How many tests would you like to clear?"))

