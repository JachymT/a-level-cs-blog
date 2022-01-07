# Programming techniques

## Subroutines
Subroutines (procudures and functions) are blocks of code that carry out a a set of named instructions. They are definded in psydocode code with: 

```
procedure name(parameters)
  //code sequence
endprocedure

name(arguments)
```

**parameters** are defined locally in the function and **arguments** give values to parameters as they are passed in, either by reference or value

a **function** differenciates from a procedure because it returns a value

**Advantages of Subroutues**
- easier to write and understand 
- easier to debug and test
- modular and decomposition programming - breaking down a problem into smaller problems
- resusable in the file and across files by importing as a module
- efficiency

## Recursion
Subroutines that reference themselves. These have the potential to loop infinitly until a a stopping condition is met (base case). Ontop of this stacks are placed in memory containing variable 

```py
def factorial(n):
  if n == 0:
    return 1
  else:
    prev = factorial(n-1)
    fact = n * prev
    return fact
```

## Iteration
A block of code is executed a certain number of times or while a condition is met. Iteration uses FOR, WHILE or REPEAT UNTIL loops. It often replaces recursion, for some solutions its can be more optimal and intuitive.

```py
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result = fact * i
  return fact
```


