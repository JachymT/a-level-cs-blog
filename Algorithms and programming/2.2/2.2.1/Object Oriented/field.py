# field simulation encompass all previous classes into one management menu

from potato import *
from wheat import *
from sheep import *
from cow import *
import random

class Field:
    """Simulate a field with cattle and crops"""

    # constructor
    def __init__(self,maxAnimals, maxCrops):
        self._animals = [] 
        self._crops = []
        self._maxAnimals = maxAnimals
        self._maxCrops = maxCrops

    def add_crop(self,crop):
        if len(self._crops) < self._maxCrops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._maxAnimals:
            self._animals.append(animal)
            return True
        else:
            return False
        
    def remove_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        cropReport = []
        animalReport = []
        for crop in self._crops:
            cropReport.append(crop.report())
        for animal in self._animals:
            animalReport.append(animal.report())
        return {"crops": cropReport,"animals": animalReport}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
                
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water = needs["water need"]
        
        return {"food":food, "light": light, "water":water}

    def grow_field(self,food,light,water):
        for crop in self._crops:
            crop.grow(light,water)

        #food must be shared between animals to grow
        foodTotalNeed = 0
        for animal in self._animals:
            needs = animal.needs()
            foodTotalNeed += needs["food need"]
        if food > foodTotalNeed:
            extraFood = food - foodTotalNeed
            food = foodTotalNeed
        else:
            extraFood = 0

        for animal in self._animals:
            needs = animal.needs()
            if food >= needs["food need"]:
                food -= needs["food need"]
                feed = needs["food need"]
            else: 
                feed = 0

            # effecitvely useless, but distributes the extra food uneavenly
            if extraFood > 0:
                extraFood -= 1
                feed += 1
            animal.grow(feed,water)
        

def display_crops(cropList):
    print("\nCrops growing in this field:")
    index = 1
    for crop in cropList:
        print("{0}. {1}".format(index,crop.report()))
        index += 1

def display_animals(animalList):
    print("\nAnimals chilling in this field:")
    index = 1
    for animal in animalList:
        print("{0}. {1}".format(index,animal.report()))
        index += 1

def select_crop(listLen):
    validOption = False
    while not validOption:
        try:
            choice = int(input("Please select a crop\n > "))
            if choice in range(1,listLen+1):
                validOption = True
            else:
                print("Invalid option entered, please enter again")
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice - 1

def select_animal(listLen):
    validOption = False
    while not validOption:
        try:
            choice = int(input("Please select a animal\n > "))
            if choice in range(1,listLen+1):
                validOption = True
            else:
                print("Invalid option entered, please enter again")
        except ValueError:
             print("Invalid option entered, please enter again")

    return choice - 1

def remove_field_crop(field):
    if len(field._crops) > 0:
        display_crops(field._crops)
        selected = select_crop(len(field._crops))
        return field.remove_crop(selected)
    else:
        print("no crops in field")
        return "not"

def remove_field_animal(field):
    if len(field._animals) > 0:
        display_animals(field._animals)
        selected = select_animal(len(field._animals))
        return field.remove_animal(selected)
    else:
        print("no animals in field")
        return "not"

def add_field_crop(field):
    choice = display_crop_menu()
    if choice == 1:
        if field.add_crop(Potato()):
            print("\ncrop planted")
        else:
            print("\ncrop failed to plant - field is full")
            
    if choice == 2:
        if field.add_crop(Wheat()):
            print("\ncrop planted")
        else:
            print("\ncrop failed to plant - field is full")

def add_field_animal(field):
    choice = display_animal_menu()
    if choice == 1:
        if field.add_animal(Sheep()):
            print("\nanimal aquired")
        else:
            print("\nanimal failed to be aquired - field is full")
            
    if choice == 2:
        if field.add_animal(Cow()):
            print("\nanimal aquired")
        else:
            print("\nanimal failed to be aquired - field is full")


def auto_grow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow_field(food,light,water)

def manual_grow(field):
    print("Enter a light value between 1-10 for the whole field")
    light = get_menu_choice(0, 10)
    print("Enter a water value between 1-10 for the whole field")
    water = get_menu_choice(0, 10)
    print("Enter a food value between 1-100 for the animals")
    food = get_menu_choice(0, 100)

    for i in range(10):
        field.grow_field(food,light,water)

def display_crop_menu():
    print("Which type of crop would you like to add")
    print("\n1. Potato\n2. Wheat\n0. Return to previous menu")
    return get_menu_choice(0, 2)

def display_animal_menu():
    print("Which type of animal would you like to add")
    print("\n1. Sheep\n2. Cow\n0. Return to previous menu")
    return get_menu_choice(0, 2)

def display_main():
    print("\n1. Plant a crop\n2. Harvest a crop")
    print("\n3. Add an animal\n4. Remove an animal")
    print("\n5. Grow field manually (10 days)\n6. Grow field automatically (30 days)")
    print("\n7. Report field status\n8. Report field needs")
    print("\n0. Exit Program")
    return get_menu_choice(0, 8)

def get_menu_choice(lower, upper):
    validOption = False
    while not validOption:
        try:
            choice = int(input("\n> "))
            if lower <= choice <= upper:
                validOption = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
             print("Invalid value entered, please enter again")

    return choice

def manage_field(field):
    print("Welcome to the field management program")
    end = False
    while not end:
        menu = display_main()
        if menu == 1:
            add_field_crop(field)
        elif menu == 2:
            removed = remove_field_crop(field)
            print("Crop {0} removed".format(removed))
        elif menu == 3:
            add_field_animal(field)
        elif menu == 4:
            removed = remove_field_animal(field)
            print("Animal {0} removed".format(removed))
        elif menu == 5:
            manual_grow(field)
        elif menu == 6:
            auto_grow(field,30)
        elif menu == 7:
            print(field.report_contents())
        elif menu == 8:
            needs = field.report_needs()
            for key, value in needs.items():
                print(key, " : ", value)
        elif menu == 0:
            end = True
    print("\nSee you next time")
        
def main():
    field1 = Field(3,12)
    manage_field(field1)

if __name__ == "__main__":
    main()
