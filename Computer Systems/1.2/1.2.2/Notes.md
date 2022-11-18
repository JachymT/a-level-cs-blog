# Application Generation

## Translators
high level source code needs to be translated to low level object code (machine code)

![image](https://user-images.githubusercontent.com/72783315/201951276-340b3416-b2e1-4125-a1de-852e85606222.png)

### Compilers
C++ is an example of a compiled language. Source code is translated into an executable all at once, for a specific architecture.

**Advantages**
- Executable can be run instantly - code does not have to be re-translated
- Executables are better optimised - runs faster
- Compilers produce executable code that cannot easily be read back into the origional - if the executable is shared, the source code is protected

**Disadvantages**
- Code cannot be compiled if there is an error which make debugging slow for large programs
- Need to recompile for new versions
- Different verions of the executable need to be made for different architectures, however this only requires different compilers and so is not too difficult.

### Interpreters
JavaScript is an example of an interpreted lanauge. Code is translated and executed line by line.

**Advantages**
- Code can be run on any architecture
- Becuase code is also error checked line by line, errors are shown as they occur and the program will stop at any error so its easy to tell which line it came from. This makes them useful for debugging.

**Disadavntages**
- Execution is far slower than with translators. 
- They also require an interpreter at run time, which takes up space in memory.

### Intermediate code
Java is an example of a language compiled to intermediate code and executed on a virtual machine. This means it can be used on any device with a Java Virtual Machine. 

**Advantages**
- Intermediate code is often simply a better way to interpret code.

### Assemblers
Translates a program written in assembly language into machine code.

### Test
