# Application Generation

## Translators

### Compilers
C++ is an example of a compiled language. Compilers produce executable code that cannot easily be read back into the origional - if the executable is shared, the source code is protected. Different verions of the executable need to be made for different architectures, however this only requires different compilers and so is not too difficult. 

This is the fastest way to run code because once compiled, the executable can be run instantly, and the code does not have to be re-compiled.

Code cannot be compiled if there is an error which make debugging slow for large programs.

### Interpreters
JavaScript is an example of an interpreted lanauge. Code is translated line by line. Code can be run on any architecture

Becuase code is also error checked line by line, errors are shown as they occur and the program will stop at any error so its easy to tell which line it came from. This makes them useful for debugging.

Interpreters are far slower than other translators. They also require an interpreter, which takes up space in memory.

### Intermediate code
Java is an example of a language compiled to intermediate code and executed on a virtual machine. This means it can be used on any device with a Java Virtual Machine. Intermediate code is often simply a better way to interpret code.

https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.2/1.2.1/notesVM.md
