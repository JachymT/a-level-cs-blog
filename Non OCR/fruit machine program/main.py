# Fruit machine program, computer science booklet, challenge 5
# 24.09.2021

import random

def generateRoll(options):
    rolls = []
    for i in range(3):
        roll = random.choice(options)
        rolls.append(roll)
    return rolls

def isCreditSuff(bal):
    if bal < 20:
        return False
    else:
        return True

def game():
    result = 0
    pool = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
    slots = generateRoll(pool)
    print("\n|| {0} || {1} || {2} ||\n".format(slots[0],slots[1],slots[2]))

    for i in pool:
        if (slots.count(i) == 2):
            if i == "Skull":
                result = -50
            else:
                result = 50
            break

        if (slots.count(i) == 3):
            if i == "Skull":
                result = -100
            elif i == "Bell":
                result = 500
            else:
                result = 100
     
    if result >= 0:
        print("you won {0} credits".format(result))
    else:
        print("you lost {0} credits".format(result))
    return result

def main():
    credit = 100
    cont = " "

    print("Welcome to the Fruit Machine")
    print("you have 100 credits, roll to win more! Each roll costs 20.")

    while cont != "no":
        credit -= 20
        credit += game()
        if isCreditSuff(credit):
            print("you have {0} credits".format(credit))
            cont = input("do you want to roll again (yes/no)")
        else:
            cont = "no"
    
    print("you've run out of credits :(")
    
if __name__ == "__main__":
    main()