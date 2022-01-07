# Programming techniques

## Subroutines
Subroutines (procudures and functions) are blocks of code that carry out a a set of named instructions. They are definded in psydocode code with: 

```
procedure name(parameters)
  //code sequence
endprocedure

name(arguments)
```

**parameters** are defined locally in the functio and **arguments** give values to parameters as they are passed in, either by reference or value

a **function** diffferenciates from a procedure because it returns a value

**Advantages of Subroutues**
- easier to write and understand 
- easier to debug and test
- modular and decomposition programming - breaking down a problem into smaller problems
- resusable in the file and across files by importing as a module
- efficiency

## Recursion
Subroutines that reference themselves. These have the potential to loop infinitly until a astopping condition is met. 

```
def factorial(n):
  if n == 0:
    return 1
  else:
    prev = factorial(n-1)
    result = n * prev
    return result
```

## Iteration
A block of code is executed a certain number of times or while a condition is met. Iteration uses FOR, WHILE or REPEAT UNTIL loops. It often replaces recursion, for some solutions its can be more optimal and intuitive.
