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
Programs need to recieve a **fair** amount of processor time, processes aren't **starved** and processes aren't **deadlocked** by eaiting for each other to release recources.The OS is responsible for using a scheduling algorithm decide where in the running state queue programs are placed.

Scheduling algorithms can be pre-emptive - where a 

### Round Robin
Each program is given a time slice slice (quantum

### First come first serve
The queue simply works in a linear order

### Multilevel feedback queues

### Shortest job first
The shortest programs are scheduled first. They are evaluated based on thier length

### Shortest remaining time
Like shor
