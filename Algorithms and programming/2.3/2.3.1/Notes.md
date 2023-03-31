# Algorithms

## Big O notation
Big O notation is used to classify the order of an algorithm, messuring how runtime or space requirements grow as the size of data scales - it aproximates growth. Big O notation is a non machine dependent. Whilst big O is an indicator of efficieny, its only really applicable for large data sets (large values of n). An O(n²) algorithm can be equally fast compared to am O(log n) algorithm for 5 items. O(n²) should still be avoided if there is a better alternative.

Big O notation can refer to best case, worse case or the average case. Worst case senario is most commonly used because you can't expect your algorithm to run with the best case or average case all of the time. Average can be ambigous - for example in a linnear search your item might not even be in the list. Worst case is the easiest the calculate and covers all cases.

- O(1) constant; doesn't scale (maths operations)
- O(log n) - logarithmic time; changes at a slowing rate (divide and conquer)
- O(n) - linnear time; changes proportionally to the input (linnear search)
- O(n log n) - linearithmic time; between n and n² (merge sort and quicksort)
- O(n²) - polynomial time; proportional to the square, has a nested loop (bubble sort)
- O(2ⁿ) - exponential time; amount of time doubles as n increased, slower than polynomial (recursive algorithms are 2ⁿ, fib recursive is 1.618ⁿ without optimisations!)
- O(n!) - factorial time; just don't (traveling salesman brute force solution... and bogosort)
- O(nⁿ) - super-exponential; mind blown emoji

To find the time complexity of an algorithm, check the time complexity of each loop and and count how many operations are made (how many lines of code are roughly executed). Then take the highest degree of this function and omit any constants. If you found there to be a total of f(n) = ½n(n+1) operations, then the big O notation would be O(n²). O(n²) should usually be avoided.

Space complexity? Don't worry about it. Considers auxiliary (temporary) space and any additional inputs the algorithm takes.

## Designing algorithms
An algorithm is a sequence of steps to solve a problem. It should terminate and handle as many cases as possible. A good algorithm should be unambigous, understandable and optimised as far as possible. 

Consider time and space compexity (using a lot of storage is bad and memory is limited), in unison. One can be sacrifised for the other sometimes. Memory is not as scarce as time generally and space is not an issue for small data sets. Time complexity is more important for real time systems.

**Tractable algorithms** - have a feesable solution with predicatable efficiency.
- Can be messured with time and space complexity. 
- Actual definition is that it is achievable in polynomial time complexity or less. 
- E.g a searching a finite list.

**Intractable algorithms** - not solveable in a reasonable amount of time. 
- Can be approximated with heuristics like when trying to plot a graph - not every value can be calculated so the shape needs to be estimated with points. 
- Or algorithsm with high time complexities like towers of Hanoi, bin packing and prime factor decompositon of large numbers. These have exponential time complexities or higher.
- Or subjective problems like finding the meaning of life.

## Searching algorithms

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
Bubble sort has muliple passes through a list. Makes comparisions between all pairs of items and swaps them if not in order. This ends up with the largest item moving to the end with each pass. Bubble sort terminates with one final pass where no swaps are necessary.
- O(n²) time complexity
- Slowest sort

```py
A = [13,4,0,2,16,7]

for i = 0 to A.length - 1
  for j = 0 to A.length - 2
      if A[j] > A[j+1] then
         swap A[j] and A[j+1]
      endif
  next j
next i
```

### Insertion Sort
Insertion sort considers sorted and unsorted parts of the list. Moving through the list, each time another element is individually added to the sorted list. One element is sorted at a time basically.
- Efficient for small lists, and nearly sorted lists
- O(n²) time complexity - still just as slow as bubble sort for large lists
- takes very little storage / overhead
- Insertion sort is an **adaptive** algorithm, its time complexity is O(n) when a list is nearly sorted

ie. The start of the list is sorted, up to the number of passes that have happened. The nth item is compared to every item to the left of it.

```py
13, 4, 0, 2, 16, 7   # 13 is sorted, 0 passes
4, 13, 0, 2, 16, 7   # 4, 13 are sorted, 1 pass
4, 13, 13, 2, 15, 7  # list is moved over to the write and then correct element is inserted at the end
4, 4, 13, 2, 15, 7
0, 4, 13, 2, 15, 7   #0, 4, 13 are sorted, 2 passes
...
```

### Merge Sort
Merge sort works by spliting a list into two smaller lists recursively untill the list have a length of 1. These sublists then considered sorted, and can be merged with adjacent sorted sublists. Lists are merged in a way to keep them sorted. The final remaining list is sorted and fully merged.
- Divide and Conquer
- Recursive
- Efficient O(n logn)

*Recursion happens in the split step*
```py
     8, 2, 4, 1        # split
   8, 2     4, 1
  8    2   4    1
   
   2, 8     1, 4       # merge
     1, 2, 4, 8
```

### Quick Sort
Quick sort starts by choosing a central pivot element in the list. Then elements are placed either side of the pivot, and are sorted in relation to that pivot. This is recursively repeated with new pivots untill there are no more elements that could become the pivot, because only elements that havn't been pivots before can become pivots, and only elements thats have elements that have not become pivots next to them. Pivots automatically get sorted.
- recursive
- O(n²) worst case time complexity
- Average O(nlog n) time complexity if optimised

*pivot chosen randomly*
```py
16, 6, 5, 22, (11) pivot = 11
6, 5, (11), 16, 22

6, (5)
(5), 6  = sorted

16, (22)
16, (22) = sorted

5, 6, 11, 16, 22
```

### Time complexity guide

![image](https://user-images.githubusercontent.com/72783315/225045690-e07edd77-c459-4901-adca-538f4f2d2d90.png)

## Path finding algorithms
Finding the shortest route from one point to another, when having to travel across other points. Path finding algorithms work on weighted graph structures and can be applied to satnavs, puzzle solving, packet routing and even finding the shortest length of wire for a a circuit. They avoid costs in the form of slower paths. E.g if there was an obstance in one of the roads and the weight was raised to 100, path finding algorithms would go around that road, same with a wall.

### Dijkstra
Finds the shortest path from a start node to any other node. Implemented using a priotity queue.

Method
- Start node has a distance of 0
- The neighbouring nodes are checked.
- Once nodes are removed from the queue, that is their final distance
- The final values are teh distances from the start node to each node.
- To find the path, go backwards subtracting the weight of the edge if it gives the node final value. E.g  from D=8 you want to go along an edge of length 1 to C=7 since 8-1=7

Implemented using a priotity queue.

### A*
The A* algorithm is a more general dijkstra's algorithm used to find a specific node, rather than all nodes in a graph. Uses heuristic approach to better direct where Dikstra searches. Uses aproximate distance, for example using as the crow flies distances for aproximation. Imagine raises nodes up to make a hill going towards the node you want to find. For example if you want to drive to Edinburgh, you don't need to search any nodes to the south. 

