import random

#creating the class
class Crop:
    # Docstring
    """Crop Class""" 

    # constructor
    def __init__(self,growthRate, lightNeed, waterNeed):

        #set the attributes with initial values
        #self refers to itself (the class)
        #private variables
        self._growth = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._lightNeed = lightNeed
        self._waterNeed = waterNeed
        self._status = "Seed"
        self._type = "Generic"

    # Creating methods, which are functions attached to a class
    def needs(self):
        # returns a dictionary
        return {"light need":self._lightNeed, "water need":self._waterNeed}

    def report(self):
        return {"type":self._type, "status":self._status, "growth":self._growth, "daysGrowing":self._daysGrowing}

    def grow(self,light,water):
        if light >= self._lightNeed and water >= self._waterNeed:
            # grow crop
            self._growth += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

    # Private method shown by _
    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"

    def return_type(self):
        return self._type

# you can pass an instance into a function
def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

# try except error handling
def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Enter a light value (1-10): "))
            if 1 <= light <= 10:
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

    crop.grow(light,water)

# User menu for testing
def display_menu():
    print("\n1. Grow crop manually\n2. Grow automatically over 30 days\n3. Report Status\n0. Exit program")

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

def manage_crop(crop):
    # print("currectly managing {0} crop".format(crop.return_type()))
    end = False
    while not end:
        menu = display_menu()
        if menu == 1:
            manual_grow(crop)
        elif menu == 2:
            auto_grow(crop,30)
        elif menu == 3:
            print("crop needs", crop.needs())
            print("crop report", crop.report())
        elif menu == 0:
            end = True
    print("See you next time")
    
def main():
    # instanciate the class
    newCrop = Crop(1,4,3)
    manage_crop(newCrop)

if __name__ == "__main__":
    main()
