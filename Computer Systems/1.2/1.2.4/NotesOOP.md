# Object Oriented Programming
Object Oriented Programming is a programming aproach that more closely models the real world, compared to procedural language. The fundemental concept of OOP is using objects to solve problems and carry out computations, by manipulating the objects and modelling data (relationships between objects).

## Comparing OOP and procedural programming paradigms in development

link

## Attributes
Attributes model characteristics of an object like we would use variables or data structures in structured programming. They are peices of data that describe each instance of a class. Simply, they are vars in a class

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

Child classes (ussually, kinda idk) can't inherit private attributes from parent class.

### Class diagrams

![image](https://user-images.githubusercontent.com/72783315/155695435-937a0bed-ad0e-4394-8b94-3c6e67551e10.png)

[good video, details not specific to course](https://www.youtube.com/watch?v=UI6lqHOVHic)

## Instantiation
Creating instances of a class can be done to create as many objects as needed

![image](https://user-images.githubusercontent.com/72783315/155984540-da38a184-e17c-47f2-9dfa-d53eae2ea65d.png)

## Encapsulation
Hides the details of implementation from the user, so the user doesnt need to know how the program works. Encapsulation is the binding of attributes and methods so that data is **protected**. It means that everything should be contained inside the class and is not accessed directly.

**Private** variables are an example of encapsulation, Allows for **data integrity** and security as it **prevents the accidental change** of variables and **data validation** can be implemented on any parameters entered. 

Encapsulation is achieved using **getter and setter methods**.

## Inheritance
Allows to build on pre-existing work, which is advantageous. A child class inherits and reuseses functionality and characteristics from a parent class, including attributes and methods. A child class can have additional methods and attributes.

![image](https://user-images.githubusercontent.com/72783315/152790871-5843f096-a881-40f2-9594-1b5fd9d08ecb.png)

Inheritance diagrams use arrow heads to point up to the parent classes

## Polymorphism
In a child class, amending methods from the parent class overrides them and lets the program use the same names for similar methods, even though they are different. This is called polymorphism, and is done by adding a method in a child class with the same name as the method in the parent class. 

It is the ability to process objects differently depending on thier class or data type.

Litterally, polymorphism is occurring in many different forms.

## OOP in Python
Following OOP python tutorial: http://pythonschool.net/oop 

[to make this field class](https://github.com/JachymT/a-level-cs-blog/blob/main/Algorithms%20and%20programming/2.2.1/Object%20Oriented/field.py)

**Notes**

```py
# For a child class
def __init__(self,param1, param2)
  super().__init__(param1, param2)      # Super refers to the parent class through a temporary object
                                        # this is how the constructor works for inheritance
```

```py
# The below is useless and you'll never need it
from pprint import pprint                   # Module for printing variables from class objects neatly
pprint(vars(object_instance))
```

## OOP psudeocode 
varaibles and procedures / function must be preceded with `private` or `public`. Constructors are given the name `new` and should be public. Self is never used in psudeocode.

```py
class Pet
  private name
  public procedure new(givenName)
    name = givenName
  endprocedure
endclass
```

**Inheritance**

Use `inherits` key word when declaring class and class `super.new()` in the constructor

```py
class Dog inherits Pet
  private breed
  public procedure new(givenName, givenBreed)
    super.new(givenName)
    breed = givenBreed
  endprocedure
endclass
```

**Instantiating**

Use `new` key word on its own to instanciate a class object

```py
myDog = new Dog("Cramberry", "Hampter")
```

## Practise papers

[Mrs Azizi on 23/05, completed in class kept by teacher](https://classroom.google.com/c/Mzg4MTUwMjc3MTA5/a/NTIxMjA1NTA4NzQ5/details)
