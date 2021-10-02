#python summer work
#mastermind random number guesser challenge
import random

def generateRandom():
    return random.randint(1000,9999)

def guessInput():
    guess = 0
    while len(str(guess)) != 4:
        guess = int(input("enter a 4 digit number:"))
    return guess

def digitcheck(guess,randomNum):
    match = 0
    for i in range(4):
        if str(guess)[i] == str(randomNum)[i]:
            match = match + 1
    return match

def main():
    randomNum = generateRandom()

    guess = guessInput()
    attempts = 1

    while guess != randomNum:
        match = digitcheck(guess,randomNum)
        print ("you guessed", match, "digits correctly")
        guess = guessInput()
        attempts = attempts + 1
        
    print("you guessed correctly in", attempts, "attempts\n")
    return

if __name__ == '__main__':
    print("Welcome to mastermind, guess a random 4 digit number\n")
    again = "yes"
    while again == "yes":
        main()
        again = input("do you want to play again (yes/no)")
