# Programming techniques

## Programming constructs
Sequencing - code is executed line by line in order

Branching - a block of code is run if a condition is met, an algorithm makes a choice

Iteration - a block of code is run a certain number of times or untill a condition is met

## Subroutines
Subroutines (procudures and functions) are blocks of code (modules) that carry out a a set of named instructions. They are definded in psydocode code with: 

```py
procedure name1(parameters)
  //code sequence
endprocedure

name1(arguments)

function name2(parameters)
  //code sequence
endfunction

name2(arguments)
```

a **function** differenciates from a procedure because it returns a value

**Advantages of Subroutines**
- easier to write and understand 
- easier to debug, test and maintain
- resusable in the file and across files by importing as a module
- efficiency

**modular** and decomposition programming is breaking down a complex problem into smaller more managable, self-contained problems (modules). The top-down approach seperates a program into further sub-problems untill each task is a single unit.

## Passing parrameters

**parameters** are defined locally in the function and **arguments** give values to parameters as they are passed in, either by reference or value

```py
function main(var:BYVAL)
  var += 1
endfunction
```

When passing **by value**, the variable is essentially duplicated. The variable inside the function is a copy, held at a new memory location, and the old variable is unchanged. This creates a local scope variable and is same as defining the variable inside the function.

```py
function main(var:BYREF)
  var += 1
endfunction
```

When passing **by referance**, a pointer is created to access the origional variable from inside the function, by holding the memory location of the argument. This extends the scope of the variable and changing the parameter affects the variable passed.  

## Recursion
Subroutines that reference (call) themselves. These have the potential to loop infinitly until a a stopping condition is met (the **base case**). Then the function starts to unwind, from stacks are placed in memory containing variables with data in sequence of recursion. If the recursion doesnt have a base case, a **stack overflow** error occurs.

```py
def factorial(n):
  if n == 0: 
    return 1                             #base call
  else:
    fact = n * factorial(n-1)            #recursive call            
    return fact
    
def fib(n):
    if n <= 1:
        return 1                         #base call
    else:
        return (fib(n-1) + fib(n-2))     #recursive call
```

## Iteration
A block of code is executed a certain number of times or while a condition is met. Iteration uses FOR, WHILE or REPEAT UNTIL loops. It often replaces recursion, for some solutions its can be more optimal and less complex.

```py
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result = result * i
  return result
  
def fib(n):
    a, b = 0, 1
    c = 0
    for i in range(0, n):
        c = a + b
        a = b
        b = c
    return c
```

NOTE: you can practive converting iterative algorithms to recusrsive ones.

## Variable scope
The scope of a varaible refers to its regeion of accessability.

**Differences between Local and Global**
- Local variables are easier to debug than golbal varaibles due to them being contained to a shorter section of code
- Local varaibles are much more secure, unexpected changes to the varaibles wont occur to them outside of thier function
- Local variables with the same names as global variables take precedence over them.
- Global variables make it harder to integrate modules
- Global variables increase the complexity of a program
- Global variable names may clash and cause conflicts, local variables can have the same name in different functions
- Global variables can be seen anywhere in the program

![image](https://user-images.githubusercontent.com/72783315/149768085-f22d77bb-d805-4ee4-a060-4a6df581afd8.png)

