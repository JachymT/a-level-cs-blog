# Data structures

## Arrays
An array in an **ordered**, **static**, of elements of a **single type**.

### One dimensional arrays
1D arrays are linnear arrays, are defined as follows (in pseudocode):

```py
array numbers[4]
numbers[2] = 19
numbers[3] = 5
print(numbers[3])

>> 5
```

### Multi dimensional arrays
2D arrays are indexed in python as `numbers[1][2]` or in psuedo code `numbers[1,2]`

```py
array numbers[3,3]
numbers[1,0] = 4
print(numbers[1,0])

// numbers = [[6, 8, 1], [4, 98, 31], [45, 7, 7]] not sure if this is allowed, just use a list

>> 4
```

3D arrays can be visualised as multi-page spreadsheets and can bethought of as multiple 2D arrays, in psuedo code arr[1,2,3]

```py
array numbers[2,2,2]
numbers[1,0,1] = 4
print(numbers[1][0][1])

// numbers = [[[6, 8,], [4, 98,]], [[45, 7,],[0, 5]]]

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

// dont access like an array ?
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

![image](https://user-images.githubusercontent.com/72783315/167635691-63f6e5ab-fbaf-4733-893e-3a3a171d1465.png)

### Operations
Must be able to:
- Add a node - add the end of the list, and then re-arrange pointers
- Delete a node - keep the list the same, re-arrange pointers
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

## Trees
![image](https://user-images.githubusercontent.com/72783315/168257022-a7303f2f-d6ae-4ea0-a485-ffc20c3cf228.png)
![image](https://user-images.githubusercontent.com/72783315/168257817-6b046204-4b0c-4bfc-925b-b98f7e3f45c4.png)

Starts with a **root node**, and has nodes coming off it with **branches**

Used for **path finding algorithms** and **file systems**.

### Binary trees
Special case of a tree, where it can only have 2 child nodes. This is the most commen way to use trees and the only way you need to know for the exam. They are much easier to search through and use a **left pointer and a right pointer**, which can be implemented using a 2D array.

Used in:
- binnry search
- database applictions
- wireless networking
- OS scheduling
- compression algorithms

If using a binnary tree to sort data, compare each item to the node, and then go left if < and right if >, then add it to the end

### Operations
- Add a node - If using a binnary tree to sort data, compare each item to the node, and then go left if < and right if >, then add it to the end.
- Remove a node - Delete the node and then re-arrange all the items below to follow the same rules as the origional tree
- binary search 
- bredth-first search - 
- pre-order traversing
- post-order traversing
- in-order traversing

https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm

### Pre-order traversing (Depth first)
Start at the **root** node, Traverse the **left** sub-tree, Traverse the **right** sub-tree

![image](https://user-images.githubusercontent.com/72783315/168823124-18340a32-8b4a-466d-843b-2cbee3cf28a1.png)

Method: Draw an arrow around the tree and follow it, writing any node it passes.

### Post-order traversing
Traverse the **left** sub-tree, Traverse the **right** sub-tree, Visit the **root** node

![image](https://user-images.githubusercontent.com/72783315/168833206-b5665720-c050-4267-adfa-dd80fbee3164.png)

Method: Draw an arrow around and follow it BACKWARDS, writing any node it passes in reverse order. So going round backwards and writing the list backwards

### in-order traversing
Traverse the **left** sub-tree, Visit the **root** node, Traverse the **right** sub-tree

Method: Just write out the list in the correct order. Don't try and traverse.

Note: there are better ways to do traversal, learn the dot method.

### Bredth first traversal
Make notes: 

https://isaaccomputerscience.org/concepts/dsa_pathfinding_dfs_bfs?examBoard=all&stage=all

### Implementation
[Recursive implementation in python](https://github.com/JachymT/a-level-cs-blog/tree/main/Computer%20Systems/1.4/1.4.2)

Based on this tree

![image](https://user-images.githubusercontent.com/72783315/169520322-225dd11c-87df-47ba-b29e-f48cf5f3c625.png)

[Read This for psuedocode](http://faculty.cs.niu.edu/~mcmahon/CS241/Notes/Data_Structures/binary_tree_traversals.html)

## Properties
**Static data structures** - size of the data structure is set cannot be changed during run time. Elements in **contiguous** (adjacent) memory locations

**dynamic data structures** - size is not limited and can be changed during run time. Elements are stored in **non-contiguous** memory locations

Dynamic offers the most efficient use of memory, and the most flexibility, However it can overflow if memory runs out. Dynamic is also harder to program as size and location needs to be kept track off.

**Mutable** - data inside the structure can be changed during run time

**Immutable** - data inside the structure cannot be changed during run time

**ordered** - can be accessed using indexing, can be assumed to be **zero indexed**

**finite set** - memory can overflow (citation needed)
