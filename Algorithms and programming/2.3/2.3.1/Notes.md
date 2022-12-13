#Algorithms

## Searching algorithms
Find a specified element form a data structure.

### Linnear Search
Searches every index of the list sequencially, comparing the desired item to every element in the list, starting with the first, and moving on untill the item is found or the end of the list is reached.
- List does not need to be sorted
- O(n) time complexity - inefficient
- easy to implement

```py
list = [5, 17, 31, 4, 21, 18]
find = 21

for i=0 to list.length-1 
  if list[i] == find then
    return i // item found at list index i
  endif
next i

// item not found in list
```

### Binary Search
Splits a list by the middle element untill the item is found
- List needs to be sorted 
- O(log n) time complexity

// python implmentation
