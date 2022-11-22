# Application Generation

## Stages of translation
high level source code needs to be translated to low level object code (machine code). 

<img src="https://user-images.githubusercontent.com/72783315/201951276-340b3416-b2e1-4125-a1de-852e85606222.png" height="300">

<img src="https://user-images.githubusercontent.com/72783315/202662440-29edb18e-df09-408a-adb7-473497a71739.png" height="400">

**Assemblers** - Translates a program written in assembly language into machine code.

**Libraries** - Pre-written modules for high level langauges that provide additional functuality efficiently and reliably.

**Dynamic Link Libraries** - A library shared by multiple programs. DLLs  are linked to the translated program by the OS. DLLs reduce the amount of main memory needed because the DLLs can be used repeatedly. DLLs are used to load drivers by programs. 

**Linkers** - When an program produces multiple code objects, a linker resolves them all into 1 executable.#

**Loader** - Before a program can be executed, the loader needs to prepare the machine code, so that it can be loaded into main memory.

## Oder of translation
4 main stages for going though the diagram above

### Lexican analysis
Removes comments, whitespaces and formats code into individual words (lexemes). Creates a series of tokens from 

### Syntax analysis
Checks oder of expressions and syntax. Matches tokens against set rules of the language, e.g. identifier must be followed by a varaible name - int score. Detects any syntacs errors. Creates an abstract syntax tree (parse tree).

### Code generation
Abstract tree code -> object code. Object code can then be linked (see above).

### Code optimisation
Optimised by changing machine code control flow to get rid of redundant instructions. Makes machine code run as quickly as possible using as little memory as possible.

![image](https://user-images.githubusercontent.com/72783315/203333009-50b3d3eb-e8f7-436c-9530-5dd174028a1e.png)

## Compilers
C++ is an example of a compiled language. Source code is translated into an executable all at once, for a specific architecture.

**Advantages**
- Executable can be run instantly - code does not have to be re-translated
- Executables are better optimised - runs faster
- Compilers produce executable code that cannot easily be read back into the origional - if the executable is shared, the source code is protected
- Therefore best for selling software

**Disadvantages**
- Code cannot be compiled if there is an error which make debugging slow for large programs
- Need to recompile for new versions
- Different verions of the executable need to be made for different architectures, however this only requires different compilers and so is not too difficult.

## Interpreters
JavaScript is an example of an interpreted lanauge. Code is translated and executed line by line.

**Advantages**
- Code can be run on any architecture
- Becuase code is also error checked line by line, errors are shown as they occur and the program will stop at any error so its easy to tell which line it came from. This makes them useful for debugging.
- software can still be shared over a browser - JS is not completly useless.

**Disadavntages**
- Execution is far slower than with translators. 
- They also require an interpreter at run time, which takes up space in memory.

## Intermediate code (Bytecode)
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
