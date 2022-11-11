# Thinking Concurrently
**Concurrent processing** - one program does not have to finish before another starts. Can be done on a single processor.

Multitasking is a systems when the illusion is given to simultaneously execute multiple tasks at once by swithcing porcesess in and out the processor. Concurrent processing can be multitasking on multi core systems. This is used when multiple applications are running, or two things need to be reacted to at once. Similar to what the OS does.

Parallel processing is slightly different. Parallel is ACTUALLY simultaneous.

![image](https://user-images.githubusercontent.com/72783315/201316379-b430fd19-eb62-432e-bb59-76a6ce3853fe.png)

![image](https://user-images.githubusercontent.com/72783315/201315693-93b8b33f-fde7-45d2-95b3-4597528baafb.png)


### Advantages
- Multiple cores working on multiple tasks at once improves overall performance.
- More efficient use of processor time - idle time is reduced
- Fewer bottlenecks - processes in the blocked state can give way to processes being executed simultaneuosly
- Multithreading is more efficient for linked tasks that needs lots of components calculated without having to wait for each one to finish individually

### Disadvantages
- Processes competing for recourses have to wait.
- Concurrent tasks do not require inputs to feed into each other

## Multithreading

