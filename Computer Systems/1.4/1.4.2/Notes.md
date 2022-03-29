# Data structures

## Arrays
An array in an **ordered**, **static**, **finite set** of elements of a **single type**. Arrays are always **zero indexed** and values in adjacent memory locations

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

## Properties
**Static data structures** - size of the data structure is set cannot be changed during run time
**dynamic data structures** - size is not limited and can be changed during run time

Dynamic offers the most efficient use of memory, and the most felxibility, However it can overflow if memory runs out. Dynamic is also harder to program as size and location needs to be kept track off.

**Mutable** - data inside the structure can be changed during run time

**Immutable** - data inside the structure cannot be changed during run time
