# Structure and function of the processor

## Control Unit
The CU directs the operations of the CPU, including:
- Handling the flow of data and instructions
- Manages all of the inputs and outputs between the CPU and other devices
- Controlling the activites of the registers
- Accepting the next instructions
- Decoding and executing instrutions 
- Storing data in memory

The CU coordinates the fetch decode execute cycle through sending control signals via busses to registers. It accepts and decodes instructions and stores the data in memory. It manages the flow of the CPU.

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
PC holds the address of the next instruction to be executed. Could be the address of the next instruction in RAM. At the start of the fetch-decode-execute cycle its copied to the MAR.

IMPORTANT: **After sending the value to the MAR, the PC is incremented, or if a jump instruction takes place, the PC is changed to the address held in the CIR**

### Memory Address register
MAR holds the **memory location (address)** of data or an instruction which will be fetched next.

### Memory data register
MDR is a temporary data store. It holds data that has been fetched from memory, or will be sent to memory. Any data that comes through the CPU enters the MDR.

### Current instruction register
CIR holds the current instruction being executed. If an instruction is fetched from the MDR it will be moved to the CIR. The instructions need to be decoded since they are made up of binary opcodes and operands

### Accumulator
Holds the data and control information, for example results of calculations from the ALU. Its a general purpose register - there are lots of these in the CPU, and the more there are the faster  Alternative uses are as a buffer or for temporary storage.

### Status register 
Holds the information about the state of the proccessor.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.1/images/2.png">

## Busses
Very Thin wires that link the CPU and its components to main memory via parallel wires. They are responsibe for fetching and sending data. Use the the word **carries**

### Address bus
Unidirecional -> bus that carries the addresses of the data that is being read or writen to main memory.

### Data bus
Omnidirectional <-> bus that carries instructions and data to and from main memory. This is the data that the CPU has or will process.

### Control bus
Omnidirectional <-> bus that carries control signals and commands from the CU to registers in the CPU, for example a signal that a program is requesting bus access. 
