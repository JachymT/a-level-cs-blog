# Scheduling
In oder to multitask and execute threads simultaniously, the operating systems needs a scheduler. Scheduler manages which programs execute next and for how long. Multitasking achieves the illusuion of simultanious execution by rapidly switching between programs. Processes are held in memory, suspended, untill they become running software

## Process states
- Only one process can be run at a time - assigned the **running** state
- Processes in the queue are wating for CPU time - assigned the **runnable/ready to run** state
- Processes wating for an I/O to contuinue, such as hard drive access - assigned the **Blocked/Suspended** state

The suspended state is less common and needs to be managed seperatly to not block up the queue. Processes will wait in the blocked queue untill there is an interupt which it can use. It can then be moved straight into the ready to run queue.

![image](https://user-images.githubusercontent.com/72783315/145560818-29f9b4dc-f81b-47a1-8da3-6459630d8b19.png)

### Runnable state
It is up to the scheduler with the use of an scheduling algorithm to decide on which programs to place where in the queue. Any programs in the state are already loaded into main memory.

### Running state
Whislt running, a program can do several things to exit the running state
 - Complete the task and close.
 - Be interupted by the scheduler. This is not the same as an interupt, this is the OS telling the program to stop using the CPU and be placed back into the runnable queue. This could also be the program running out of its alocated time
 - Become blocked and move out of the CPU to avoid wasting time
 - Give up CPU time volunterily

## Scheduling algorithms
Programs need to recieve a **fair** amount of processor time, processes aren't **starved** (by not getting any processor time) and processes aren't **deadlocked** (by waiting for each other to release recources). The OS is responsible for using a scheduling algorithm to decide where in the running state queue programs are placed. Algorithms become more complex when factoring in multiple cores

Scheduling algorithms can be **pre-emptive** - where jobs can be actively cut off from their processing time by the operating system.

It is not possible to rank these algorithms, they can be favoured in different situations and make trade offs between, least wait time, maximum throughput and maximum fairness.

### First come first serve
Jobs are added to the end of the queue and executed in order of arival, from the front of the queue. The order is strict and the programs may have to wait a long time.

Generally inefficient for using recources, but easy to implement.

### Round Robin
Each program is given a time slice (**quantum**) of processor time. After the time slice the program is moved back to the end of the queue.

This method spreads out processing time and gives all processes fair amount of time. Innefficient for long programs and generally

### Shortest job first
Programs are evaluated based on thier length and the shortest ones are scheduled at the front of the queue and executed in oder from shortest to longest. Relies on the CPU knowing how long an algorithm will take, which it can only predict

### Shortest remaining time
Works exactly like Shortest job first, other than that this algorithm is pre-emptive. When a process is suspended in the CPU and returns to the queue, its remaining time is evaluated and its placed in its respective place in the queue.

This reduces risk of starvation because once longer programs get processor time, they increase their priority and wont get stuck at the back of the queue. 
Pre-empting programs is common, so this algorithm is advantagous to shortest job first.

The downside is that sequencing the queue often is an expensive calculation.

### Multilevel feedback queues
By creating multiples queues with levels of priority, for example 0 being high, 1 being medium and 2 being low, the scheduler can move jobs up and down levels based on a set of rules. Processes are typically added in a FCFS fashion into the highest priority queue and then moved down or up, but not jumping postions in queue.

<img width="874" alt="Scheduling algs" src="https://user-images.githubusercontent.com/72783315/146681676-341a08b7-5caa-4d09-bda6-69cdab17fd1d.png">
