# Algorithms

## Searching algorithms
Find a specified element form a data structure.

### Linnear Search
Searches every index of the list sequencially, comparing the desired item to every element in the list, starting with the first, and moving on untill the item is found or the end of the list is reached.
- List does not need to be sorted
- O(n) time complexity - inefficient for large data sets
- easy to implement

```py
list = [5, 17, 31, 4, 21, 18]
find = 21

for i=0 to list.length-1 
  if list[i] == find then
    return i #item found at list index i
  endif
next i

#item not found
```

### Binary Search
Splits a list by the middle element. Compares the desired item to the midpoint. If it is the correct value, then the seach is completed. Otherwise, check if its less than or greater than the value, and discard the half of the list that isn't needed. From here repeat with the smaller list, untill the desired item is found or if it is not in the list.
- List needs to be sorted 
- Divide and conquer approach - list is split and then values are compared
- O(log n) time complexity - fast for large data sets

```py
list = [5, 17, 31, 4, 21, 18]
find = 21

low = 0
high = list.length - 1

while low <= high then
  mid = (low + high) / 2 # round up
  
  if list[mid] == find then
    return mid # item found at list index mid
  endif
  
  else if list[mid] > find then
    high = mid - 1  # removes 2nd half of list
  endif
  
  else if list[mid] < find then
    low = mid + 1  # removes 1st half of list
  endif
endwhile

#item not found
```

## Sorting algorithms
Useful for different senarios so learn to compare

https://www.toptal.com/developers/sorting-algorithms

### Bubble Sort

### Insertion Sort

### Merge Sort

### Quick Sort
