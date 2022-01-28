# potato module interits from the crop class module 

from crop import *

class Potato(Crop):
    """Potato Crop"""

    def __init__(self):
        # call the parent (superclass) constructor with defult values for potatoes
        # growth rate = 1, light need = 2, water need = 6
        super().__init__(1,2,6)
        self._type = "Potato"

def main():
    potatoCrop = Potato()
    manual_grow(potatoCrop)
    print(potatoCrop.report())

if __name__ == "__main__":
    main()
