# Data structures

## Arrays
An array in an **ordered**, **static**, of elements of a **single type**, in a **contiguous** area of memory. They allow for indexing and using values under a single identifier.

You do not need to use an equals sign for declaring arrays in pseudocode. Identifiers are baked in when declaring

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

numbers = [[6, 8, 1], [4, 98, 31], [45, 7, 7]] #not sure if this is allowed, just use a list

>> 4
```

3D arrays can be visualised as multi-page spreadsheets and can bethought of as multiple 2D arrays, in psuedo code arr[1,2,3]

```py
array numbers[2,2,2]
numbers[1,0,1] = 4
print(numbers[1][0][1])

numbers = [[[6, 8,], [4, 98,]], [[45, 7,],[0, 5]]]

>> 7
```

## Lists
A list is an **dynamic**, set of elements which can **occur more than once**, and be of **more than one data type**. They are like 1D arrays in that they are **zero indexed** and are accessed in the same way.

They can be manipulated using various functions for example in psuedocode:
```c#
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
Queues also handle linear lists of data. They use a **first in first out** (FIFO) data structure. They are implemented using 2 pointers, one to the end (**tail pointer**) and one to the start (**head pointer**). Can be of fixed or dynamic length. Queues can also be circular, and so the pointers can both loop around. The same commands for stacks can be applied for queues. 

Priority queues allow for jumping to the front of the queue, giving all data a priority before enqueuing and then comparing priorities.

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

Prodecural implementation would just be using a 2D array passed to and from functions.

## Hash tables
Hash tables are used in dictionaries and let data be found from a list in O(1) time. Hashing is used in database indexing, and storing passwords.

<img width="626" alt="hash table" src="https://user-images.githubusercontent.com/72783315/222905253-276df27e-f6a3-4f2d-a2c6-20fc0d532d21.png">

### Hash functions
Position of data in a hash tables is calculated with a **hash function** / **hashing algorithm**. Hash tables are just arrays, accessed as normal, but they require key-value pairs. This is becuase the hash fucntion needs to be applied to a **key** coresponding to the value, to get a new memory address in the array. The key is not the actual array position!!! 

If there is no key one can be made out of the value by adding up its ASCII if its a string, or is a key is a string the same is done. This is all done by the hash function. If the key is not the value itself it should be stored with with value.

Hash function using a MOD:
```py
(key, value) -> make the key hashable -> key MOD length of array -> hash value / position / bucket
```

A hash function should:
- return the same array position for the same key
- be fast to compute
- use little memory
- have a uniform distribution of hash values (array positions)
  - therefore result in **few collisions** - where unique keys result in the same hash value 
  - and minimsl clustering - where the table gets filled up in common collision spots.
  - if every single value collided, every search would be a linnear search which defeats the point.
- Also they are one way (cannot be undone easily)

Hash tables are larger than the number of items in the table, optimally by about x1.33. The larger the number of postions in the array the more space is wasted, but the more free room the table has to store all the data with a lower chance of getting an collision.

### Operations
Searching, adding and removing values in a hash table is very efficient and simple. Infact they all do the same thing and work in one operation. Put the key through the hash function, get the index in the array, check for collions and complete the operation.

### Collisions
One way to deal with the inveitable fate of meeting a collision is to replace the hash table with pointers to linked lists. This is called **chaining** / closed addressing and is shown in the diagram above. Nodes in the linked list store the key, value and pointer to the next node. This makes dealing with colliosns easy since you just go down the list until you fin the item you want or you find a null pointer.

The second way is to use **linnear probbing** / open addressing. This just moves down the hash table untill an open spot is found for the data to go, but this can end up getting in the way of other data. This reduces efficeiny, esspecially for a small hash table since when searching, indexes are checked untill an empty one is found.

### Re-hashing
Creating a new table with the optimal number of spaces for the new amount of data items. Instead of a hash table filling up and getting slow, all the values can be recalculated to improve overall efficiency.

## Graphs
Graphs are a set of nodes (vertices) and edges (arcs), representing relationships between objects, such as transport networks, molecular structures and routers. They are **abstract data structures** (they are not coded the same way they are represented).

![image](https://user-images.githubusercontent.com/72783315/224493438-5cc37300-7491-49c1-9d25-336ebc404b19.png)

**adjacent** - neighbouring nodes connected by an **edge / arc**

**degree** - the number of connections a node has

**path** - a sequence of connected nodes

**cycle** - a part of a graph is cyclical if a node has a path back to itself, without crossing the same node twice

### Undirected graphs
Straight up a normal graph, can be traversed in both directions. One way to implement in code using a dictionary, called an **adjacency list**. Each key is a node and the values are its neighbouring nodes. Alternative representation is as a list with pairs of nodes, representing edges. The notation below works for directed graphs by only having values that the nodes points to in the dict.

```py
DICTIONARY graph = {
  "1" : ["2", "3"],
  "2" : ["1", "3", "5"],
  "3" : ["1", "2", "4"],
  "4" : ["3"], 
  "5" : ["2"]
}

edges = { (1,2), (1,3), (2,3), (2,5), (3,4) }
```

### Directed graphs
Edges point in a direction from one node to another. Drawn with arrows

All graphs, even weighted, can have both directed and undirected parts in the same graph, although they usually use omni directional arrows to show that.

### Weighted graphs
Edges are given values. In a transport example with cities as nodes these are not distances! they are simply the cost of the journey in relation to the other journeys, eg the average time it would take from that node to the next. They can be represented as matrixes or lists.

#### Adjacency matrixes
Adjacency matrixes are tables (arrays) of all possible connections between nodes, with each cell being an edge. They are great for visualling paths, adding new nodes or just getting information from them! Example of a weighted undirected graph as an adjacency matrix below with a real life application !!!! !!!! !! ! ! ! 

<img width="625" alt="celeste lobby routing" src="https://user-images.githubusercontent.com/72783315/224494584-90b556ad-c71f-4ab5-ae13-35eb8fa07a14.png">

#### Adjacency lists
Adjacency lists are more space efficient for large graphs, since you don't have a bunch of empty spaces in the array. They are just dictionaries / the way that graphs are stored normally, except with edge values.

![image](https://user-images.githubusercontent.com/72783315/224496012-ae41d088-b0d1-4d90-84f3-1791b9847a34.png)

### Graph traversals
Traversals systematically explore each node in a graph. Each node can be in 1 of three states: unvisted, discovered and visited. unvisted nodes can be added to a list of nodes to explore next. Discovered nodes have been added to a list / seen because one of its neighbours was previously visited and visted nodes have been fully explored and can be marked off.

Practise implementing these.

#### Bredth first
Uses a **queue** to decide which node to visit next. Visits all adjacent nodes before moving on. Similar to dikstra's but slightly different. Remember to only add nodes to the queue if they havnt been discovered yet. Search ends when all nodes have been visted.

#### Depth first
Uses a **stack** to decide which node to visit next. Visits all nodes down a path before backtracking. Can be done recursively or iteratively.

## Trees
Trees are just graphs with extra rules. Specifically, a connected undirected graph with no cycles. Used for **path finding algorithms** and **file systems**. They can be 

![image](https://user-images.githubusercontent.com/72783315/168257022-a7303f2f-d6ae-4ea0-a485-ffc20c3cf228.png)

tree facts: 
- Rooted trees starts with a **root node** which has no nodes coming into it. All trees can be rooted however it just depends on how its drawn.
- **branches** connect nodes
- Nodes can be **parents** or **children** depending on if they have branches coming in or out.
- A **leaf** has no children
- A **subtree** is a tree contained in a tree.

### Binary trees
Special case of a tree, where each node can have a max of 2 child nodes. This is the most commen way to use trees and the only way you need to know for the exam. They are much easier to search through and use a **left pointer and a right pointer**, which can be implemented using a 2D array.

A **binnary search tree** is an **ordered**, **balanced** binnary tree. Balanced means it splits in two perfectly. The smaller the **height** of a tree (how many subtrees deep it) the optimised the tree is for searching.

An in order traversal gives the nodes in ascending order, and a reverse in order traversal gives descending values. If using a binnary tree to sort data, compare the item to each node, and then go left if < and right if >, then add it to the end.

![binnary search tree](https://user-images.githubusercontent.com/72783315/216965893-072c4c5d-c139-457a-94ba-c59d7f2e8ae6.png)

Used in:
- binnary searches
- database applictions
- wireless networking
- OS scheduling
- compression algorithms
- postfix notation - where operators go after the operands. There is also an infix and postfix notation. Infix is jsut normal arithmetic so use that to check (uess inorder)

### Operations
These are the same for graphs. Note: traversing is the same as searching!!

- Add a node - If using a binnary tree to sort data, compare each item to the node, and then go left if < and right if >, then add it to the end.
- Remove a node - Delete the node and then re-arrange all the items below to follow the same rules as the origional tree
- bredth-first traversing (same as for graphs) 
- depth first traversing (all start at the root node and explore as far a possible before backtracking)
  - pre-order traversing
  - post-order traversing
  - in-order traversing 

The order for when the root node is visited () is the same as the order in which you draw the dots when traversing. Also left node is always checked before the right node. 

![image](https://user-images.githubusercontent.com/72783315/224696393-37d7dd95-83e7-4638-b03d-1e1a49cb4cf2.png)

Use method 1 for traversing the above. The order is pre then in then post, from left to bottom to right, the same as the position of the ↓ in the algorithm! Its easy!

#### Pre-order traversing ↓ ← →
Visits a node before exploring its subtrees (traverses going down). Start at the **root** node, traverse the **left** sub-tree, traverse the **right** sub-tree ↓ ← →

Method 1: Draw an line around the tree and go in order of the **left** dots (red)

Method 2: Draw an arrow around the tree and follow it, writing any node it passes. (the same as method 1)

#### in-order traversing
Nodes are visited between the subtrees. Gives ordered data if the tree is ordered with the lowest values as the root. Traverse the **left** sub-tree, visit the current node, traverse the **right** sub-tree ← ↓ →

Method 1: Draw an line around the tree and go in order of the **bottom** dots (blue)

Method 2: Just write out the list in the correct order. Don't try to traverse.

#### Post-order traversing
Node is visited after both of its subtrees. Traverse the **left** sub-tree, traverse the **right** sub-tree, visit the current node ← → ↓

Method 1: Draw an line around the tree and go in order of the **right** dots (green)

Method 2: Draw an arrow around and follow it backwards, writing any node it passes in reverse order. So going round backwards and writing the list backwards.

### Implementation
[Recursive implementation in python](https://github.com/JachymT/a-level-cs-blog/tree/main/Computer%20Systems/1.4/1.4.2)

Based on this tree

![image](https://user-images.githubusercontent.com/72783315/169520322-225dd11c-87df-47ba-b29e-f48cf5f3c625.png)

[Read This for psuedocode](http://faculty.cs.niu.edu/~mcmahon/CS241/Notes/Data_Structures/binary_tree_traversals.html)

## Properties
**Static data structures** - size of the data structure is set cannot be changed during run time. Elements in **contiguous** (adjacent) memory locations. Easier to porgram than dynamic structures

**dynamic data structures** - size is not limited and can be changed during run time. Elements are stored in **non-contiguous** memory locations

Dynamic offers the most efficient use of memory, and the most flexibility, However it can overflow if memory runs out. Dynamic is also harder to program as size and location needs to be kept track off.

**Mutable** - data inside the structure can be changed during run time

**Immutable** - data inside the structure cannot be changed during run time

**ordered** - can be accessed using indexing, can be assumed to be **zero indexed**

**finite set** - memory can overflow (citation needed)
