# Structure and function of the processor

## Registers

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.1/images/1.PNG">
![image](https://user-images.githubusercontent.com/72783315/134178364-876cc0f6-2734-4402-8b6c-a97b7cb1e5fe.png)

### PC
Program counter holds the address of the next instruction to be executed. Could be the address of the next instruction in RAM. At the start of the fetch-decode-execute cycle its copied to the MAR

### MAR
Memory Address register holds the **memory location (address)** of data or an instruction which will be fetched next.

### MDR
Memory data register is a temporary data store. It holds data that has been fetched from memory, or will be sent to memory. Any data that comes through the CPU enters the MDR.

### CIR
Current instruction holds the current instruction being executed. If an instruction is fetched from the MDR it will be moved to the CIR. The instructions need to be decoded since they are made up of binary opcodes and operands

### ALU
Arithmatic logic unit

### Accumulator

## assembly language

## Machine code instructions

### Opcodes
### Operands

## relationship between assembly language and machine code
