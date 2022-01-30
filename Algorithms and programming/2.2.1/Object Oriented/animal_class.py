#clone of crop_class
import random

#creating the class
class Animal:
    # Docstring
    """Animal Class""" 

    # constructor
    def __init__(self, growthRate, foodNeed, waterNeed):

        #set the attributes with initial values
        #self refers to itself (the class)
        #private variables
        self._weight = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._foodNeed = foodNeed
        self._waterNeed = waterNeed
        self._status = "Baby"
        self._type = "Generic"

    # Creating methods for reporting
    def needs(self):
        return {"food need":self._foodNeed, "water need":self._waterNeed}

    def report(self):
        return {"type":self._type, "status":self._status, "weight":self._weight, "daysGrowing":self._daysGrowing}

    #grow the animal
    def grow(self,food,water):
        if food >= self._foodNeed and water >= self._waterNeed:
            self._weight += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

    # Private method shown by _
    def _update_status(self):
        if self._weight > 40:
            self._status = "Old"
        elif self._weight > 20:
            self._status = "Mature"
        elif self._weight > 10:
            self._status = "Young"
        elif self._weight > 5:
            self._status = "Child"

    def return_type(self):
        return self._type

# you can pass an instance into a function
def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

# try except error handling
def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input("Enter a food value (1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
            print("Invalid value entered, please enter again")
            
    valid = False
    while not valid:
        try:
            water = int(input("Enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
            print("Invalid value entered, please enter again")

    animal.grow(food,water)

# User menu for testing
def display_menu():
    print("\n1. Grow animal manually\n2. Grow automatically over 30 days\n3. Report Status\n0. Exit program")

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

def manage_animal(animal):
    #nprint("currectly managing {0} animal".format(animal.return_type()))
    end = False
    while not end:
        menu = display_menu()
        if menu == 1:
            manual_grow(animal)
        elif menu == 2:
            auto_grow(animal,30)
        elif menu == 3:
            print("animal needs", animal.needs())
            print("animal report", animal.report())
        elif menu == 0:
            end = True
    print("See you next time")
    
def main():
    # instanciate the class
    newanimal = Animal(1,4,3)
    manage_animal(newanimal)

if __name__ == "__main__":
    main()
