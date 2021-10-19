# Pipelining in a CPU

Pipelining is the process of creating a series of accumlated instructions to continously process instructions across multiple CPUs. Instructions are proccessed parallelly and are overlapping during execution. The **latency**, time taken for a single instruction to be proccessed, remains the same.

![https://youtu.be/RuenPZT1PyM](https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.1/images/3.PNG)

## Inside the CPUs 
Instead of fetching instruction A, the decoding instruction A, then excecuting isnstruction A. With pipeline processing the CPU does not wait for A to be finished executing before moving onto B

## advantages
- Pipelining increases the overall instruction throughput and the overall speed of the CPU
- The cycle time for each instruction is reduced, since each part of the CPU is always processing something.

## Probelems
- Data dependencies in the sequence can cause problems. If the previous isntruction is requied for the next for it may not be availiable
- Branching in a program 
- this lead to a proccess called flushing the pipe - where the currect instructions beuing processed in the CPU are abondoned and the process restarts

![https://youtu.be/RuenPZT1PyM](https://user-images.githubusercontent.com/72783315/137920053-f9b677b1-5020-4ea8-8a37-6a1dc6dc4a99.png)

**Further reading**

https://whatis.techtarget.com/definition/pipelining
