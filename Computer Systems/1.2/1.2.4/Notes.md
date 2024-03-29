#  Types of Programming Languages
Languages are classified into programming paradigms based on how they aproach problem solving.

Imperitive - Programmer instructs the machine on exactly what actions to perform

Declerative - Programmer declares the desired result and not the instructions on how to get to it. The language decides how to reach the outcome and how abstracted the process is.

Turing Complete - A languge is turing complete if it can solve any compuational problem. Popular languages are all turing complete.

![image](https://user-images.githubusercontent.com/72783315/170046543-a1b5265b-4337-46d0-b20c-918090fc1de3.png)

### Procedural
Procedural langauges are common and apply to a wide range of problems. Easy to **implement** and **interpret**. Sequences of instructions are executed line by line. The key features of **structured procedural programming** are: sequence, selection, iteration and recursion.

Examples: Pascal and C

### Object Oriented
[https://github.com/JachymT/a-level-cs-blog/edit/main/Computer%20Systems/1.2/1.2.4/NotesOOP.md](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.2/1.2.4/NotesOOP.md)

Examples: C++ and Java

### Comparing OOP and procedural programming paradigms in development

**Advantages of OOP**
- For games and simulations - where objects frequently interact with each other
- More closely models the real world. Eg a farms attributes and behaviours 
- Classes can be re-used and extended with child classes. Advantageous if you have pre-written classes to use. Encourages code integrity.
- Highly modular (encourages splitting functionality into smaller, compatable and individual pieces)
- Therefore easy to maintain
- Provides data protection from encapsulation. Prevents careless and harful access to private variables
- Therefore more data integrity than Procedural

https://isaaccomputerscience.org/concepts/prog_oop_why?examBoard=ocr&stage=a_level&topic=object_oriented_programming

**Advantages of Procedural**
- OPP can result in complex systems, procedural is better for simpler programs.
- Libraries of subroutines can be imported, so code is re-useable
- Program flow and self documantation is better
- Subroutines can share data and manipulate it repeatedly
- top-down problem-solving aproach - often decompositional

### Functional
Use the concept of calling functions multiple times, and only using functions to get an output from an input. Mostly used to handle giant data sets. An example is Haskell.

### Logic
Use queries to solve problems after defining a set of rules. An example is Prolog.

## Assembly language
Assembly language is a programming language that uses meumonics to comunicate with the CPU, and so has to be specific to the CPU. It is a low level language that can be converted into machine code with an assembler. Useful for writing real time embedded systems.

[Little Man Computer instructions and code](https://github.com/JachymT/a-level-cs-blog/tree/main/Computer%20Systems/1.1/1.1.1/Little%20Man%20Computer)

For example, in LMC, if you wanted to load the value at address 3 you would write `LDA 003`. Machine code works similarly. 

### Comparing low level and high level languages in development

**Low Level**
- architecture specific
- fastest possible execution time
- small storage requirements
- for embedded systems / OS development
- control hardware directly

**High Level**
- easier to use and learn
- easeir to maintain and debug
- very specialised to solve certain problems
- produces software fast

## Machine code instructions
Binary instructions that the CPU can process, specific to the type of CPU. All programs are translated into machine code. An instruction in machine code contains an opcode and operand part, these are **split in the Current Instruction Register** (CIR). These can be seen more clearly in **assembly language** which is a simplified view of machine code.

### Opcodes
The opcode specifies the type of instruction to be executed.

### Operands
The operand specifies the data or address to be processed.

## Modes of Memory Addressing
Memory addressing is used to get data from the CPU or RAM. Used explicitly in low level languages. They descripe how the operand is used.

### Immediate
Nothing is fetched in immediate addressing, data is given directly in the instruction. 

- Fastest method of adressing 
- Useful for constants

### Direct
Uses the locations in memory for the operand. Needs to know where the data is stored. LMC uses direct adressing

- Also a fast method of adressing
- Can't be used if data is being moved around in memory

### Indirect
Uses an intermediate vector table. Address points to a location which holds the actual address.

- Used for accessing code in external libraries

### Indexed
Index determined by a base address with an ofset added to it. 

- Locating data from arrays or chunks of data in memory
- Fast and very useful
- Only base address need to be changed and indexes stay the same when the program is re-located

Relative addressing is the same as indexed, expect the offest is relative to ther current address, held in the program counter. E.g jpm +5
