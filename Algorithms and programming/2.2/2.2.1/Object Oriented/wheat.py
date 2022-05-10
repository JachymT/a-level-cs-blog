# potato module interits from the crop class module 
from crop_class import *

class Wheat(Crop):
    """Wheat Crop"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for wheat
        # growth rate = 3, light need = 4, water need = 2
        super().__init__(3,4,2)
        self._type = "Wheat"

    #override grow method for this subclass (polymorphism)
    def grow(self,light,water):
        if light >= self._lightNeed and water >= self._waterNeed:
            # added functionality to adjust for different crop type
            if self._status == "Young" :
                self._growth += self._growthRate * 1.5
            elif self._status == "Mature" :
                self._growth += self._growthRate * 2
            else:
                self._growth += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    wheatCrop = Wheat()
    manual_grow(wheatCrop)
    print(wheatCrop.report())

if __name__ == "__main__":
    main()