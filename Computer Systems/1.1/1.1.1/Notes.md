# Structure and function of the processor

## Control Unit
The CU directs the operations of the CPU, including:
- Handling the flow of data and instructions
- Manages all of the inputs and outputs between the CPU and other devices
- Controlling the activites of the registers
- Accepting the next instructions
- Decoding instrutions 
- Storing data in memory

## Cache 
Stored close to or inside the CPU. It is very rapid access memory that holds commenly stored instructions and programs.

### Arithmatic logic unit
ALU performs operations on data. Including 
- arithmatic operations like ADD, SUBTRACT, MULTIPLY and DIVIDE;
- bitwise shifts
- Boolean operations like AND, OR, NOT

## Registers
Registers are small memory cells that operate at a very high speed. They are used to temporarily store data.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.1/images/1.PNG">

### Program counter
PC holds the address of the next instruction to be executed. Could be the address of the next instruction in RAM. At the start of the fetch-decode-execute cycle its copied to the MAR

### Memory Address register
MAR holds the **memory location (address)** of data or an instruction which will be fetched next.

### Memory data register
MDR is a temporary data store. It holds data that has been fetched from memory, or will be sent to memory. Any data that comes through the CPU enters the MDR.

### Current instruction register
CIR holds the current instruction being executed. If an instruction is fetched from the MDR it will be moved to the CIR. The instructions need to be decoded since they are made up of binary opcodes and operands

### Accumulator
Holds the data and control information, for example results of calculations from the ALU. Its a general purpose register - there are lots of these in the CPU.

### Status register 
Holds the information about the state of the proccessor.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.1/images/2.png">

## Busses
Very Thin wires that link the CPU to main memory. They are responsibe for fetching and sending data.

### Address bus
...

### Data bus
...

### Control bus
...

## Assembly language
Assembly language is a programming language that used meumonics to comunicate with the CPU. For example if you wanted to load instruction 4 you might write LDA 0100. It is a simplified view of Machine code, which is more understandable for people. An instruction contains an opcode and operand part, which is split in the CIR. 

### Opcodes
The opcode specifies the type of instruction to be executed.

### Operands
The operand specifies the data or address to be processed.

## Machine code instructions
...

## relationship between assembly language and machine code
...
