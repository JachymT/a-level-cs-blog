# Programming techniques

## Programming constructs
Sequencing - code is executed line by line in order

Branching - a block of code is run if a condition is met, an algorithm makes a choice

Iteration - a block of code is run a certain number of times or untill a condition is met

## Subroutines
Subroutines (procudures and functions) are blocks of code (modules) that carry out a a set of named instructions. They are definded in psydocode code with: 

```
procedure name(parameters)
  //code sequence
endprocedure

name(arguments)
```

**parameters** are defined locally in the function and **arguments** give values to parameters as they are passed in, either by reference or value

a **function** differenciates from a procedure because it returns a value

**Advantages of Subroutines**
- easier to write and understand 
- easier to debug, test and maintain
- resusable in the file and across files by importing as a module
- efficiency

**modular** and decomposition programming is breaking down a complex problem into smaller more managable, self-contained problems (modules). The top-down approach seperates a program into further sub-problems untill each task is a single unit.

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
    result = fact * i
  return fact
  
def fib(n):
    a, b = 1, 1
    for i in range(0, n):
        a = b
        b = a + b
    return a
```

NOTE: you can practive converting iterative algorithms to recusrsive ones.

## Variable scope
The scope of a varaible refers to its regeion of accessability.

**Differences between Local and Global**
- Local variables are easier to debug than golbal varaibles due to them being contained to a shorter section of code
- Local varaibles are much more secure, unexpected changes to the varaibles wont occur to them outside of thier function
- Global variables make it harder to integrate modules
- Global variables increase the complexity of a program
- Global variable names may clash and cause conflicts, local variables can have the same name in different functions

![image](https://user-images.githubusercontent.com/72783315/149768085-f22d77bb-d805-4ee4-a060-4a6df581afd8.png)

