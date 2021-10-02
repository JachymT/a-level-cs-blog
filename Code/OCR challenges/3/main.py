# pin guessing, OCR challange 3
# 01.10.2021

from itertools import permutations

def getdigits():
    n = input("enter know digits of the PIN: ")
    return n

def main():
    print("For any order of 4 digits in a PIN, all of the possiblites will be printed")
    inp = getdigits()
    digits = [int(a) for a in inp]

    perms = list(permutations(digits))  #finds all permutaions
    perms = list(dict.fromkeys(perms))  #removes duplicats by making into a dictionary breifly

    for i in perms:
        print(i)

if __name__ == "__main__":
    main()