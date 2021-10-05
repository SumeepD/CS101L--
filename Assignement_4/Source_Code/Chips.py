import random
total = 0
turns = 0
chips = int(input("How many chips do you want to start with?:"))
while(chips > 100):
    print("That value is too high. Choose a number 1 - 100")
    chips = int(input("How many chips do you want to start with?:"))

while(1 > chips):
    print("That value is too low. Choose a number 1 - 100")
    chips = int(input("How many chips do you want to start with?:"))

wager = int(input("How many do you want to wager?:"))
while(chips < wager):
    print("The wager amount can not be greater then the amount you have.")
    wager = int(input("How many do you want to wager?:"))

while(wager < 0):
    print("Wager amount needs to be above 0")
    wager = int(input("How many do you want to wager?:"))
chips -= wager
turns += 1

random1 = random.randint(1, 10)
random2 = random.randint(1, 10)
random3 = random.randint(1, 10)
print(random1, random2, random3)
if(random1 == random2):
    print("You matched 2 reels")
    total = (wager * random1) + (wager * random2)
    print("You won/lost", total)
    chips += total
    print("Your current total is", chips)
elif(random1 == random3):
    print("You matched 2 reels")
    total = (wager * random1) + (wager * random3)
    print("You won/lost", total)
    chips += total
    print("Your current total is", chips)
elif(random2 == random1):
    print("You matched 2 reels")
    total = (wager * random2) + (wager * random1)
    print("You won/lost", total)
    chips += total
    print("Your current total is", chips)
elif(random2 == random3):
    print("You matched 2 reels")
    total = (wager * random2) + (wager * random3)
    print("You won/lost", total)
    chips += total
    print("Your current total is", chips)
elif(random1 == random2 == random3):
    print("You matched 3 reels")
    total = (wager * random1) + (wager * random2) + (wager * random3)
    print("You won/lost", total)
    chips += total
    print("Your current total is", chips)
else:
    print("You lost", wager, ", you are now at", chips)
while(chips != 0):
    wager = int(input("How many do you want to wager?:"))
    while(chips < wager):
        print("The wager amount can not be greater then the amount you have.")
        wager = int(input("How many do you want to wager?:"))

    while(wager < 0):
        print("Wager amount needs to be above 0")
        wager = int(input("How many do you want to wager?:"))
    chips -= wager
    turns += 1

    random1 = random.randint(1, 10)
    random2 = random.randint(1, 10)
    random3 = random.randint(1, 10)
    print(random1, random2, random3)
    if(random1 == random2):
        print("You matched 2 reels")
        total = (wager * random1) + (wager * random2)
        print("You won/lost", total)
        chips += total
        print("Your current total is", chips)
    elif(random1 == random3):
        print("You matched 2 reels")
        total = (wager * random1) + (wager * random3)
        print("You won/lost", total)
        chips += total
        print("Your current total is", chips)
    elif(random2 == random1):
        print("You matched 2 reels")
        total = (wager * random2) + (wager * random1)
        print("You won/lost", total)
        chips += total
        print("Your current total is", chips)
    elif(random2 == random3):
        print("You matched 2 reels")
        total = (wager * random2) + (wager * random3)
        print("You won/lost", total)
        chips += total
        print("Your current total is", chips)
    elif(random1 == random2 == random3):
        print("You matched 3 reels")
        total = (wager * random1) + (wager * random2) + (wager * random3)
        print("You won/lost", total)
        chips += total
        print("Your current total is", chips)
    else:
        print("You lost", wager, ", you are now at", chips)
        print("It took you", turns, "to run out of chips")

    

