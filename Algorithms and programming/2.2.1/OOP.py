# Following OOP python tutorial
# http://pythonschool.net/oop
# Object Oriented Programming is a concept that more closely models the real world
# Attributes model characeristics of an object like we would use variables or data structures in structured programming
# Methods model behaviours of an object like we would use functions for in structured programming
# A class defines a blueprint for these attributes and methods
# Creating instances of a class can be done to create as many objects as needed - instantiation

# creating a class
# diffenrence between public and private atributes
# private attributes are onyl know by themselves, and cannot be accesed directly outside the class
# in python however, private attributes are indicated by an _ 
# This is just a practise and not a solution, _ is an indicator to the program since python cannot implement private attributes

# Encapsulation
# Hides the details of implementation from the user
# So the user doesnt need to know how the program works
# They can control the program via a user **interface**
# They cant access anything that is locked

# Interface - controlling an object in a predefined way
# Methods allow for interaction with the object

class Crop:
    # Docstring
    """Generic food crop""" 

    # constructor
    def __init__(self,growthRate, lightNeed, waterNeed):

        #set the attributes with initial values
        #self refers to itself (the class)
        #private
        self._growth = 0
        self._daysGrowing = 0
        self._growthRate = growthRate
        self._lightNeed = lightNeed
        self._waterNeed = waterNeed
        self._status = "seed"
        self._type = "generic"

    # Creating methods, which are functions attached to a class
    def needs(self):
        # returns a dictionary
        return {"light need":self._lightNeed, "water need":self._waterNeed}

    def report(self):
        return {"type":self._type, "status":self._status, "growth":self._growth, "daysGrowing":self._daysGrowing}

    def grow(self,light,water):
        pass

    # Private method shown by _
    def _update_status(self):
        pass

def main():
    # instanciate the class
    newCrop = Crop(1,4,3)
    newCrop2 = Crop(2,2,6)

    print(newCrop.needs())
    print(newCrop.report())
    print(newCrop.report()['growth'])

if __name__ == "__main__":
    main()
    
