# Scheduling
In oder to multitask and execute threads simultaniously, the operating systems needs a scheduler. Scheduler manages which programs execute next and for how long. Multitasking achieves the illusuion of simultanious execution by rapidly switching between programs. Processes are held in memory, suspended, untill they become running software

## Process states
- Only one process can be run at a time - assigned the **running** state
- Processes in the queue are wating for CPU time - assigned the **runnable** state
- Processes wating for an I/O to contuinue, such as hard drive access - assigned the **Blocked/Suspended** state

The suspended state is less common and needs to be managed seperatly to not block up the queue

![image](https://user-images.githubusercontent.com/72783315/145560818-29f9b4dc-f81b-47a1-8da3-6459630d8b19.png)

## 
