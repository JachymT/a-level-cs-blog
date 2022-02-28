# Object Oriented Programming
Object Oriented Programming is a programming aproach that more closely models the real world. The fundemental concept of OOP is using objects to solve problems and carry out computations, by manipulating the objects and modelling data (relationships between objects).

## Attributes
Attributes model characteristics of an object like we would use variables or data structures in structured programming. They are peices of data that describe each instance of a class. They are varaibles inside a class.

### Public and private
private attributes are only know by themselves, and cannot be accesed directly outside the class, they can only be accessed within the class. in python, private attributes are indicated by an underscore prefix. This is just a practise and not a solution, _ is an indicator to the program since python cannot implement private attributes.

## Methods
Methods model behaviours of an object like we would use functions for in structured programming. Methods allow for interaction with the object.  Methods can also be public or private

## Classes
Classes defines a template for these attributes and methods. These templates are reuseable. Can have the constructor in methods as well.

### Class constructors

![image](https://user-images.githubusercontent.com/72783315/155983507-6a5bb37f-5548-4653-8867-82818da76c15.png)

Self is passed into each method - it acts as a location in reference to itself. So that variables are accessed from the class itself.
Double or singe underscores can be used in python.

Child classes can't inherit private attributes from parent class.

### Class diagrams

![image](https://user-images.githubusercontent.com/72783315/155695435-937a0bed-ad0e-4394-8b94-3c6e67551e10.png)

[good video, details not specific to course](https://www.youtube.com/watch?v=UI6lqHOVHic)

## Instantiation
Creating instances of a class can be done to create as many objects as needed

![image](https://user-images.githubusercontent.com/72783315/155984540-da38a184-e17c-47f2-9dfa-d53eae2ea65d.png)

## Encapsulation
Hides the details of implementation from the user, so the user doesnt need to know how the program works. They can control the program via a user **interface**, they cant access anything that is locked or **private**. Allows for **data integrity** and **security**. Prevents the accidental change of variables.

**Interface** - controlling an object in a predefined way.

## Inheritance
Allows to build on pre-existing work, which is advantageous. A child class inherits and reuseses functionality and characteristics from a parent class, including attributes and methods. A child class can have additional methods and attributes

![image](https://user-images.githubusercontent.com/72783315/152790871-5843f096-a881-40f2-9594-1b5fd9d08ecb.png)

Inheritance diagrams use arrow heads to point up to the parent classes

## Polymorphism
In a child class, amending methods from the parent class overrides them and lets the program use the same names for similar methods, even though they are different. This is called polymorphism, and is done by adding a method in a child class with the same name as the method in the parent class. 

It is the ability to process objects differently depending on thier class or data type.

Litterally, polymorphism is occurring in many different forms.

## OOP demonstrated
Following OOP python tutorial: http://pythonschool.net/oop

[field class run this](https://github.com/JachymT/a-level-cs-blog/blob/main/Algorithms%20and%20programming/2.2.1/Object%20Oriented/field.py)

'py
from pprint import pprint     # printing variables from class objects
pprint(vars(object_instance))
'
