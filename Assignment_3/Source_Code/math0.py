nums = list(range(1, 101))
print("Please think of a number between and including 1 and 100")
num1 = int(input("What is the remainder when your number is divided by 3?"))
while(num1 < 0 and num1 > 3):
    print("Number has to be between 1 and 3")
    num1 = int(input("What is the remainder when your number is divided by 3?"))
num2 = int(input("What is the remainder when your number is divided by 5?"))
while(num2 < 0 and num2 > 5):
    print("Number has to be between 1 and 5")
    num2 = int(input("What is the remainder when your number is divided by 5?"))
num3 = int(input("What is the remainder when your number is divided by 7?"))
while(num3 < 0 and num3 > 7):
    print("Number has to be between 1 and 7")
    num3 = int(input("What is the remainder when your number is divided by 7?"))
chosenNum =1
total1 = int(chosenNum % 3 == num1)
total2 = int(chosenNum % 5 == num2)
total3 = int(chosenNum % 7 == num3)
while(num1 != total1 or num2 != total2 or num3 != total3):
    chosenNum += 1
    total1 = int(chosenNum % 3 == num1)
    total2 = int(chosenNum % 5 == num2)
    total3 = int(chosenNum % 7 == num3)
    if (num1 == total1 and num2 == total2 and num3 == total3):
        print(chosenNum)