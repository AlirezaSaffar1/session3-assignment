print("Welcome To Dice Stimulator!")

import random

while True :
    playerdecision = int(input("What do you want?   1.roll the dice     2.exit    "))

    if playerdecision == 1:
        a = random.randint(1,6)
        print(a)
        if a == 6 :
            a = random.randint(1,6)
        else:
            break
    elif playerdecision == 2:
        break
    else:
        print("Error!")
