# field simulation encompass all previous classes into one management menu

from potato import *
from wheat import *
from sheep import *
from cow import *

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

def display_crop(crop_list):
    print("\nCrops growing in this field")
    index = 1
    for crop in cropList:
        print("{0}. {1}".format())
        

def main():
    # create an instance
    newField = Field(5,5)
    # you can contrast a sheep class because its been imported
    newField.add_animal(Sheep())
    print(newField._animals)
    newField.remove_animal(0)
    print(newField._animals)

if __name__ == "__main__":
    main()
