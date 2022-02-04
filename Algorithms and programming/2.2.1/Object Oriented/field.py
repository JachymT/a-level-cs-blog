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
    display_crops(field._crops)
    selected = select_crop(len(field._crop))
    return field.remove_crop(selected)

def remove_field_animal(field):
    display_animals(field._animals)
    selected = select_animals(len(field._animals))
    return field.remove_animal(selected)

def add_field_crop(field):
    choice = display_crop_menu()
    if choice == 1:
        if field.plant_crop(Potato()):
            print("\ncrop planted")
        else:
            pass

def auto_grow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        field.grow_field(food,light,water)

def manual_grow(field):
    light = get_menu_choice(0, 10)
    water = get_menu_choice(0, 10)
    food = get_menu_choice(0, 100)

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
    print("3. Add an animal\n4. Remove an animal")
    print("5. Grow field manually\n6. Grow field automatically")
    print("7. Report field status\n0.Exit Program")
    return get_menu_choice(0, 7)

def get_menu_choice(lower, upper):
    validOption = False
    while not validOption:
        try:
            choice = int(input("> "))
            if lower <= choice <= upper:
                validOption = True
            else:
                print("Invalid value entered, please enter again")
        except ValueError:
             print("Invalid value entered, please enter again")

    return choice
        
def main():
    newField = Field(5,5)
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_animal(Sheep())
    newField.add_crop(Potato())
    newField.add_crop(Wheat())
    for i in range(10):
        newField.grow_field(100,10,6)
        report = newField.report_contents()
        print(report["animals"])
        print(report["crops"])

if __name__ == "__main__":
    main()
