# Types of Processors

## RISC 
Reduced instruction set computer - aim to use as simple instructions to process a higher number of instructions per second.

Programs are harder to translate since the compiler is producing more lines of code. More RAM is needed to store these instructions. They use a fixed format for instructions and limited modes of addressing.

However each instruction requires less **processing power** and complicated **hardware**. In RISC proccessors more room is left for registers and cache. Since instructions are uniform in execution time, pipelinning becomes feesable.

RISC is used in portable and small proccessors. E.G ARM

## CISC

Complex instructuion set computer - aims to complete a task in as few instructions as a possible, making use of very complex instructions. 

The instructions are easy to translate from a high level language to assembly, but take more clock cycles to execute. CISC Requires less instruction cycles to get the same result as RISC. They  have variable instruction lengths and multiple address modes for instructions.

Used in security systems and automation. Eg. Intel x86 and AMD. Utilize RISC practises and microcodes.

![image](https://user-images.githubusercontent.com/72783315/137929032-43626ccc-ba85-4076-ae26-34988aba1f5a.png)

## GPUs
Graphical processing units are highly specialised to be fast and eficient for certain tasks like rendering graphics. They are made for mass calculations that take full advantage of parallel processing. They became more generic and started being used for modelling and analysis.

### Co-processors
Any additional processor used for a specialist task, working concurrently with the main CPU. A GPU is an example of a co-processor

### Single Instruction Multiple Data
SIMD is a design where single instructions operate very quickly on large data sets, so repeating operatings over and over is very efficient.

## Multicore and Parallel systems

### Chip Multicore processers
Multicore processors are a single chip with two or more independent processing units(cores)
Chip Multicore processers are further enhanced by on-chip shared cache and inter-core communication. More cores are faster at proccessing simultanious instructions.

### Parallel processing
To make use of multiple cores parallel processing systems must be implemented. This splits programs up between CPUs to run them at once and faster. This is done by threading and loggically spliting programs between CPUs


