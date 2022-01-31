# clone of potato class
from animal_class import *

class Sheep(Animal):
    """Sheep Animal"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for potatoes
        # growth rate = 1, food need = 2, water need = 6
        super().__init__(1,2,6)
        self._type = "Sheep"

    #override grow method for this subclass (polymorphism)
    def grow(self,food,water):
        if food >= self._foodNeed and water >= self._waterNeed:
            # added functionality to adjust for different crop type
            if self._status == "Seedling" :
                self._weight += self._growthRate * 1.5
            elif self._status == "Yound" :
                self._weight += self._growthRate * 1.2
            else:
                self._weight += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    sheepAnimal = Sheep()
    manual_grow(sheepAnimal)
    print(sheepAnimal.report())

if __name__ == "__main__":
    main()
