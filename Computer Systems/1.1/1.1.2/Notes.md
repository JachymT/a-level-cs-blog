# Types of Processors

## RISC 
Reduced instruction set computer - aim to use as simple instructions as possible to be executed within a single clock cycle.

The instructions are harder to translate since the compiler is doing more work and making more lines of code. More RAM is needed to store these instructions. However each instruction requires less **hardware**, **processing power**, and **energy**, meaning they executed quickly. In this architecture, more room is left for registers and cache.

Since instructions are uniform in execution time, pipelinning becomes feesable.

90% of proccessors work off of RISC

## CISC
Complex instructuion set computer - aims to complete a task in as few instructions as a possible, making use of very complex instructions. The instructions are easy to translate from a high level language to assembly, but take more clock cycles to execute.

They still appear in some desktop computers and laptops but utilize RISC practises and microcodes, since RISC proccesors are more benefical.

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


