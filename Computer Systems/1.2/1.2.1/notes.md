# Software

## Software types

### System software
Runs the computer system, provides an interface, controls hardware and peripherals.
Includes Operating systems like Windows, macOS, Linux, Android and device drivers.

### Utility software
Designed to analyze, configure and optimize a computer system.
Includes disk defragmentation, antivirus software and file manager.

### Application software
A consumer product, a software made to be distributed to many consumers.
Includes word, powerpoint, firefox.

### Custom (bespoke) software
A software designed specificaly for one user, or a company to meet all thier custom needs, more expensive than using application software.
Includes company web portals, food chain software for thier employees, netflix software for creators.

## Operating system purposes
Operating systems perform many different tasks at the base level of the computer and create an API for software to be developed on. Without them there is no access to the computer's recoures and nothing to manage them. They serve the following functions to create a platform between te user and the 

### Managing Peripherals
All hardware needs to comunicate with the computer and it cannot do this without a device driver. Inputs and outputs are translated by the driver so that the OS can control it. For example keyboards and mice need to give inputs to the computer and have custom settings to do so.

### Utility programs
Background and active helper programs that run on the software. Some utilities are key, and are loaded right away. Examples of Utility programs are:
- Disk Defragmentation
- File management
- encryption
- file compression
- installers
- system moniter

### **Memory and file management**
Alocates space for programs and makes sure the OS Kernal is loaded - the kernal makes sure memory and file management is executed correctly. Its key processes are:

- **Paging** 
- **Segmentation**
- Assigning **virtual memory**
- Moving files to and from secondary storage.
- Loading programs these program segments or pages into RAM when they are needed.

### Paging
Paging happens when moving programs into RAM, where RAM does not have an entire free space for the program. To Fit the needed gaps in RAM , RAM Is physically divied into equally sized sections. Programs are divied the same way so they can be moved between main memory and RAM.

### Segementation
Segmentation is a variation of Paging, where instead of spliting programs only on size they are split into variable sections. Memory is divied into logical chunks of varying size and these program sections can be moved in and out of availiable space in RAM.

![image](https://user-images.githubusercontent.com/72783315/144589033-8dc9abe8-ffc6-4970-89e9-c32bb50594ed.png)

modern operating systems use a combination of both. It is important to note that whilst the chunks of programs are individual, they operate as if adjacent and continous.

### Virtual Memory
Assigned areas of the hard disk act as main memory for when RAM is full. Idle or other programs are moved to virtual memory by the OS, and the virtual memory acts as a slower and larger temporary replacement RAM. Issues arise when programs need to be rapidly movied between RAM and virtual memory, since this is slow. Chunks of programs will often be moved into virtual memomry or else others could simply not be run, by segmenting and paging, these sections could be kept track of, and moved as nessesary.

### Processor management
**Multitasking** and control how processor time is divided. Programs need to run in the right order and often simultaneously. It also handles [interupts](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.2/1.2.1/notes.md#interupts).

### Security
Firewall inplementation - software that stops harmful incoming trafic and scans for outside programs trying to get access to the system.
User management - provides levels of access and a profiles for users on the Network.

### User interface
Provides a visual platform for users to interact with. A UI can be as simple or a terminal, but can also be a fully customised screen with pointers, windows, menus and icons. 

### Networking
Interfacing to other computers with WiFi and cables. Serves requests and allows access to recources such as printers and files.

## Interupts
//////

## Scheduling
///////


## Types of operating systems

### Distributed
////

### Embedded
Provide a reliable platform for specific, custom applications to run. They are compact and efficient however sacrifice customizability and limit functions that can be performed. There is very little user control, as often only one task is being performed.

Examples
- Network routers
- ATMS
- Navigation Satelites

### Multi-tasking
A single user OS that supports several user applications running at once. These are the operating systems that are on most PCs and laptops. They need to be able to swap between programs for the user, by managing multiple cores or asigning time to a single core efficiently.

Examples
- Windows
- MacOS
- Linux

### Multiuser
An Os that provides resources for multiple users to access the same system. The use of resources is controlled so that no user is limited by the others.

### Real-time
Real time OSs process applications that have critically defined time restraints. It must be fast, responsive, and know how to manage limitations. Responses need to be consistently fast and respond in a garanteed time - it is vital that the time for each operation is identical. Outputs must be completed before the next input. And unexpected events must be passed in parralel and be reacted to quickly. From what i understand - real time can be seen as an operating system that syncs up actions to a clock, since the actions it performs rely on the time.

Examples
- plane autopilet systems
- self driving cars
- scientifical instruments
- industrial systems

