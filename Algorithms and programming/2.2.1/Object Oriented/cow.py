# clone of wheat class
from animal_class import *

class Cow(Animal):
    """Cow Animal"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for wheat
        # growth rate = 3, food need = 4, water need = 2
        super().__init__(3,4,2)
        self._type = "Cow"

    #override grow method for this subclass (polymorphism)
    def grow(self,food,water):
        if food >= self._foodNeed and water >= self._waterNeed:
            # added functionality to adjust for different crop type
            if self._status == "Young" :
                self._weight += self._growthRate * 1.5
            elif self._status == "Mature" :
                self._weight += self._growthRate * 2
            else:
                self._weight += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    cowAnimal = Cow()
    manual_grow(cowAnimal)
    print(cowAnimal.report())

if __name__ == "__main__":
    main()
