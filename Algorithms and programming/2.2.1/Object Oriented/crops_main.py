# management progrom inherits from the two specific crops
# which inherit from the generic crop
from wheat import *
from potato import *

def display_menu():
    print("\nWhich crop would you like to create")
    print("1. Potato\n2. Wheat")

    validOption = False
    while not validOption:
        try:
            choice = int(input("> "))
            if 0 <= choice <= 4:
                validOption = True
            else:
                print("Invalid option entered, please enter again")
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice

def create_crop():
    choice = display_menu()
    if choice == 1:
        newCrop = Potato()
    elif choice == 2:
        newCrop = Wheat()
    return newCrop

def main():
    newCrop = create_crop()
    manage_crop(newCrop)

if __name__ == "__main__":
    main()