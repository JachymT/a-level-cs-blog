# Operating Systems

## Operating system purposes
Operating systems perform many different tasks at the base level of the computer and create an API for software to be developed on. Without them there is no access to the computer's recoures and nothing to manage them. They serve the following functions to create a platform between the user

![image](https://user-images.githubusercontent.com/72783315/145047208-4101600f-16c0-4078-9535-67651d141153.png)

### Managing Peripherals
All hardware needs to comunicate with the computer and it cannot do this without a device driver. Inputs and outputs are translated by the driver so that the OS can process requests from the device. For example keyboards and mice need to give inputs to the computer and have custom settings to do so.

The peripheral management software calls a device driver, which manages the specific device.

### Utility programs
Background and active helper programs that run on the software. Some utilities are key, and are loaded right away. Examples of Utility programs are:
- Disk Defragmentation
- File management
- encryption
- file compression
- installers
- system moniter

### **Memory management**
Alocates space for programs and makes sure the OS Kernal is loaded - the kernal makes sure memory and file management is executed correctly. key memory management processes are:

- Allocating **memory** loading programs between RAM and secondary storage
  - paging
  - segmentation
  - virtual memory - In order to allow for programs larger than RAM to run
- determine how much memory to allocate to each process that is running and reserve that space
- controlling memory use. swapping between processes and their memory space in order to provide memory access as required.
- map the logical address space to the physical address space
- protect programs

### Paging
Paging happens when moving programs into RAM, where RAM does not have an entire free space for the program. To Fit the needed gaps in RAM , RAM Is physically divied into equally sized sections. Programs are divied the same way so they can be moved between main memory and RAM.

### Segementation
Segmentation is a variation of Paging, where instead of spliting programs only on size they are split into variable sections. Memory is divied into logical chunks of varying size and these program sections can be moved in and out of availiable space in RAM.

![image](https://user-images.githubusercontent.com/72783315/144589033-8dc9abe8-ffc6-4970-89e9-c32bb50594ed.png)

modern operating systems use a combination of both. It is important to note that whilst the chunks of programs are individual, they operate as if adjacent and continous.

**Exam style Question**
**Discuss the differences between paging and segmentation in terms of their efficient use of memory (7 marks)**

Paging uses memory by slicing programs into equally sized data blocks whilst Segmentation uses memory by slicing programs up into logically divided blocks, differing in size. The OS moves these in and out of RAM, in order to manage memory. 

Paging has frames that are designed to fit parts of memory, and since they are smaller they are often more efficient and dont waste as much RAM as segmented programs. They dont have to be together since they are read by an index, but this can decrease efficiency.

Since segmentation pages are often bigger, there is less space for them in RAM, making memory management less efficiently. Segmentation allows for logical reading of code and can execute entire procedures at once potentially, which can increase efficiency.

### Virtual Memory
Assigned areas of the hard disk act as main memory for when RAM is full. Idle or other programs are moved to virtual memory by the OS, and the virtual memory acts as a slower and larger temporary replacement RAM. Issues arise when programs need to be rapidly movied between RAM and virtual memory, since this is slow. Chunks of programs will often be moved into virtual memomry or else others could simply not be run, by segmenting and paging, these sections could be kept track of, and moved as nessesary.

### Processor management
**Multitasking** and controling how processor time is divided. Programs need to run in the right order and often simultaneously, or give the illusion of running simultaneously. The OS also handles [interupts](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.2/1.2.1/notesOS.md#interupts).

### Security
Firewall inplementation - software that stops harmful incoming trafic and scans for outside programs trying to get access to the system.
User management - provides levels of access and a profiles for users on the Network.

### User interface
Provides a visual platform for users to interact with. A UI can be as simple or a terminal, but can also be a fully customised screen with pointers, windows, menus and icons. 

### Networking
Interfacing to other computers with WiFi and cables. Serves requests and allows access to recources such as printers and files.

## The Kernel
In an operating system, the lowest layer of the architecture is the kernel, between the CPU/ Memory and the applications. It links the applications and the data processing done by hardware.

Its job is to deal with the core instructions and system resources, dealing with memory management, disk storage, peripherals and low level networking.

<img src="https://user-images.githubusercontent.com/72783315/149502919-f0b06151-9c4a-4104-a7a5-af757dbbe9f8.png" width= "500">

## Interupts
An interupt is a request for processor time. Interupts let the user have better control over the computer, since otherwise they would have to wait for an aplication to finish before registering something like a keybaord input, which needs to be immediate. At the end of every fetch-decode-execute cycle there is another step the CPU taskes, and this is checking for an interupt. There are different reasons for interupts: 

<img src="https://user-images.githubusercontent.com/72783315/145054323-9fe7e95d-905f-4fd2-b151-6a11c1b279da.png" width= "700">

Hardware or software sends interupts to the CPU, and in the next CPU cycle, the interupt service routine is called, the interupt is identified and control handed over to the OS so it can be handled. The handling and processing is done by a interupt service routine. The process of dealing with an interupt is called servicing.

![image](https://user-images.githubusercontent.com/72783315/145053299-610f91aa-8828-4922-a87f-9648660c8acc.png)

### Interupt Service Routine
Each interupt has its own service routine which is executed by the OS. An interupt can also be ignored if the OS chooses to.

### priorities
If many interupts happen at once
![image](https://user-images.githubusercontent.com/72783315/145049228-6aecdd6e-697f-460e-876c-7b2f821e530e.png)

### Stack
After an interupt the CPU needs to go back to executing the program before the interupt. This is done by storing the contents of registers in a stack in RAM.
Before an interupt is serviced the data is moved to the top of the stack. The stack data structure lets interupts stack ontop of each other, and so order for the instructions to be popped from the stack is maintained.

## Types of operating systems
These types are not mutually exclusive.

### Distributed
Combines processing power of multiple computers across a network. The OS coordinates many computer processors to complete a task together. The OS works across all of these deivces

Examples
- Online shopping sites - different servers for different tasks, even though for the user they are happening on the same computer
- school and work computers

### Embedded
Provide a reliable platform for specific, custom applications to run. They are compact and efficient because they run on dedicated hardware, making them use very little memory. They sacrifice customizability and limit functions that can be performed. There is very little user control, as often only one task set is being performed.

Examples
- Network routers
- ATMS
- Navigation Satelites
- TVs
- Car engine management system
- Other consumer aplications

### Multi-tasking
A single user OS that supports several user applications running at once. These are the operating systems that are on most PCs and laptops. They need to be able to swap between programs for the user, by managing multiple cores or asigning time to a single core efficiently.

Examples
- Windows
- MacOS
- Linux

### Multi-user
An OS that provides resources for multiple users to access the same system sp that more than one user can use an OS at the same time. The OS manages the users permissions and settings for each login. The network responds to lots of users across lots of computers.

Examples
- Windows
- MacOS
- Used in a School or work setting

### Real-time
Real time OSs process applications that have critically defined time restraints. It must be fast, responsive, and know how to manage limitations. Responses need to be consistently fast and respond in a garanteed time - it is vital that the time for each operation is identical. Outputs must be completed before the next input. And unexpected events must be passed in parralel and be reacted to quickly. From what i understand - real time can be seen as an operating system that syncs up actions to a clock, since the actions it performs rely on the time.

Examples
- Plane autopilet systems
- Self driving cars
- Scientifical instruments
- Industrial systems
