# Data structures

## Arrays
An array in an **ordered**, **static**, of elements of a **single type**.

### One dimensional arrays
1D arrays are linnear arrays, are defined as follows:

```py
arr = [12, 9, 5, 27]
print(arr[3])

>> 5
```

### Multi dimensional arrays
2D arrays are indexed in python as `arr[1][2]` or in psuedo code `arr[1,2]`

```py
arr = [[6, 8, 1], [4, 98, 31], [45, 7, 7]]
print(arr[1][0])

>> 4
```

3D arrays can be visualised as multi-page spreadsheets and can bethought of as multiple 2D arrays, in psuedo code arr[1,2,3]

```py
arr = [[[6, 8,], [4, 98,]], [[45, 7,],[0, 5]]]
print(arr[1][0][1])

>> 7
```

## Lists
A list is an **dynamic**, set of elements which can **occur more than once**, and be of **more than one data type**. They are like 1D arrays in that they are **zero indexed** and are accessed in the same way.

They can be manipulated using various functions for example in psuedocode:
```py
list = [2, 3, 6, 4, 9, 9, "h", "i"]
list.length()                       //returns list length
list.pop(3)                         //removes 4th item in list
list.remove(9)                      //removes the first instance of the parameter
list.append(14)                     //appends the parameter to the end of the list
```

## Tuples
Tuples, like lists, are **dynamic** and can contain **more than one data type** but they are **immutable**. They are accessed in the same way and are used for lists that shouldn't be changed.

```py
tuple = (1, 2, "Python", function(), (12, 0))
```

## Stacks
stacks handle linnear lists of data. They use a **last in first out** data structure. They are used to reverse an action - tracking user inputs, used in iteration - like pathfinding algorithms. They are implemented using pointers, which point to the top of the stack.

Adding data to a stack **pushing**. If the stack if full a stack **overflow** error is given.

taking data off the stack is called **popping**. If the stack is empty a stack **underflow** error is given.

Viewing the top of the stack is called **peeking**.

![image](https://user-images.githubusercontent.com/72783315/165319688-20432aa0-0e4a-412c-802e-776d04c9449e.png)

## Queues
Queues also handle linear lists of data. They use a **first in first out** (FIFO) data structure. They are implemented using 2 pointers, one to the end (**tail pointer**) and one to the start (**head pointer**). Queues can also be circular, and so the pointers can both loop around. The same commands for stacks can be applied for queues. Priority queues allow for jumping to the front of the queue.

![image](https://user-images.githubusercontent.com/72783315/165319077-af1b6c8e-645c-465d-a84b-fe2619c2c026.png)

## Linked Lists
Linked lists are a **dynamic**, powerful and flexible data sctructures that are used as the foundation to implemenating other data sctructures. They consist of **nodes**, each of which contains **data** and a **pointer**, which points to the next node, and a **head pointer** which points to the first node. A **double linked list** points to the next and previous nodes and a **circular linked list** points from the first to the last node.

They are useful when you need to insert items in to the middle of a list and you dont know how many items long the list will be. They can be applied to the operating system process scheduler, **blocked state queue**, image players, music players and webbrowsers.

The dissadvantages of linked lists: **traversing a linked list is very difficult**, they don't provide random access so to find an element you need to traverse all the nodes before it which is time consuming. Additionaly they **require more memory** than arrays as they need to store a pointer and data attached to a node.

### Operations
Must be able to:
- Add a node
- Delete a node
- Move to next node
- Move to prev node
- Search the list 

### C++ implemenation
[linked lists implemenation explained](https://www.codesdope.com/blog/article/c-linked-lists-in-c-singly-linked-list/#:~:text=The%20implementation%20of%20a%20linked,which%20are%20connected%20in%20nature)

Object oriented implementation is optimal as objects use any available memory and don't need to be adjacent.

```cpp
class Node
  {
  public:
    Node( string dataInput, Node* next=NULL);
    void setData( string dataValue);
    void setNext( Node* nextNode );
  private:
    string data;
    Node* next;
  };
```

## Properties
**Static data structures** - size of the data structure is set cannot be changed during run time. Elements in **contiguous** (adjacent) memory locations

**dynamic data structures** - size is not limited and can be changed during run time. Elements are stored in **non-contiguous** memory locations

Dynamic offers the most efficient use of memory, and the most flexibility, However it can overflow if memory runs out. Dynamic is also harder to program as size and location needs to be kept track off.

**Mutable** - data inside the structure can be changed during run time

**Immutable** - data inside the structure cannot be changed during run time

**ordered** - can be accessed using indexing, can be assumed to be **zero indexed**

**finite set** - memory can overflow (citation needed)
