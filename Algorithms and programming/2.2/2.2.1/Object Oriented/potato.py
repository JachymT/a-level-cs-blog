# potato module interits from the crop class module 
from crop_class import *

class Potato(Crop):
    """Potato Crop"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for potatoes
        # growth rate = 1, light need = 2, water need = 6
        super().__init__(1,2,6)
        self._type = "Potato"

    #override grow method for this subclass (polymorphism)
    def grow(self,light,water):
        if light >= self._lightNeed and water >= self._waterNeed:
            # added functionality to adjust for different crop type
            if self._status == "Seedling" :
                self._growth += self._growthRate * 1.5
            elif self._status == "Yound" :
                self._growth += self._growthRate * 1.2
            else:
                self._growth += self._growthRate
        # update details 
        self._daysGrowing += 1
        self._update_status()

def main():
    potatoCrop = Potato()
    manual_grow(potatoCrop)
    print(potatoCrop.report())

if __name__ == "__main__":
    main()
