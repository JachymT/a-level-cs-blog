# Thinking Ahead
Thinking ahead in terms of computational thinking is the process of thorough planning of your code to ensure an efficient outcome and where possible using caching/pre-fetching.

Programs should be correct and efficient

## Inputs and Outputs
Inputs and outputs for a function need to be planned, and the format that they will be input and output needs to be specified, eg an array of integers.

![image](https://user-images.githubusercontent.com/72783315/168240480-d57ae623-c7e0-430d-a912-5fc36890cbdc.png)

## Preconditions
For example if performing a linnear or binnary search, the list should be in an indexed or ordered format. This also includes specifying variable type.

### Advantages
- Making program components reusable by good documentation. Libraries can be imported whenever and save time, costs, resources, as long as they are compatable. They  provide abstraction and are pre-built and often well tested.
- Cutting out unnecessary checks - eg checking before calling the subroutine
- Making programs easier to debug and maintain

![image](https://user-images.githubusercontent.com/72783315/168241924-942b1bf5-d98b-4263-b810-ccefbf3a9c83.png)

## Caching
Caching is a temorary storage of data, with the intention that it will be accessed again. It is much faster than retrieving data from a network. The copy of the resource can be re-used, optimising system performance significantly.

Web pages are cached by your browser if used repeatedly. They have a max age and can be stored in various locations.

Caching in computer architecture is an implemention of thinking ahead. This is where the term caching comes from, cached data is much faster to retrieve.

### Advantages
- increased speeds
- reduces bandwidth and server load

### Disadvantages
- inconsistencies can occur if origional data is updated.

## Pre-fetching
As an extention of caching, requesting data before it is needed. Algorithms need to be designed to predict when data will need to be cached, or you could do this yourself, manually in a program. eg. reading a file once in a program instea of multiple times
