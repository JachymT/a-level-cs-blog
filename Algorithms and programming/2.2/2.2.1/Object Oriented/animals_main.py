# clone of crops_main
from cow import *
from sheep import *

def display_menu():
    print("\nWhich animal would you like to create")
    print("1. Cow\n2. Sheep")

    validOption = False
    while not validOption:
        try:
            choice = int(input("> "))
            if 0 <= choice <= 2:
                validOption = True
            else:
                print("Invalid option entered, please enter again")
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice

def create_animal():
    choice = display_menu()
    if choice == 1:
        newAnimal = Cow()
    elif choice == 2:
        newAnimal = Sheep()
    return newAnimal

def main():
    newAnimal = create_animal()
    manage_animal(newAnimal)

if __name__ == "__main__":
    main()
