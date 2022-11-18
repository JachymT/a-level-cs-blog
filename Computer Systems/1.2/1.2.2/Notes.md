# Application Generation

## Translators
high level source code needs to be translated to low level object code (machine code). 

![image](https://user-images.githubusercontent.com/72783315/201951276-340b3416-b2e1-4125-a1de-852e85606222.png)

![image](https://user-images.githubusercontent.com/72783315/202662440-29edb18e-df09-408a-adb7-473497a71739.png)

**Assemblers** - Translates a program written in assembly language into machine code.

**Libraries** - Pre-written modules for high level langauges that provide additional functuality efficiently and reliably.

**Dynamic Link Libraries** - A library shared by multiple programs. DLLs  are linked to the translated program by the OS. DLLs reduce the amount of main memory needed because the DLLs can be used repeatedly. DLLs are used to load drivers by programs. 

**Linkers** - When an program produces multiple code objects, a linker resolves them all into 1 executable.#

**Loader** - Before a program can be executed, the loader needs to prepare the machine code, so that it can be loaded into main memory.

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

### Intermediate code (Bytecode)
Java is an example of a language compiled to intermediate code and executed on a virtual machine. This means it can be used on any device with a Java Virtual Machine. It is source code compiled to low level byte code and then interpreted on other machines. 

**Advantages**
- Intermediate code is often simply a better way to interpret code.
- Advantages of compiling (effieicent code and fast speeds)
- Advantages of interpreting (can be done on any machine)

##  Distribution
Will be suitable for different things. Also closed source is inherently bad.

### Open Source 
The source code is availiable to the public.

**Advantages**
- 

### Closed Source / Proprietary
The source code not availiable, when accessing the software you need a licence
