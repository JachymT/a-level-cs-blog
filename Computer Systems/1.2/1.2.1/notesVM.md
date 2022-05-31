# Virtual Machines

A virtual machine is a program that emulates a hardware or other systems. It is a software implementation of a computer system.

A VM can replicate any hardware so that software can run on it, without knowing it isnt really accesing certain devices, and thinks its oh its own hardware - imagine an emulator.

## Examples
- Running alternative operating systems
- Supporting older, incompatable software 
- Creating a controlled environment for analysing potential malware
- **Virtual servers** - running multiple servers on a single peice of hardware. Eg a company that provides email and web servers. The load can be managed by the hardware sesrvers at will, if a server goes down the virtual servers can move to a different physical server.
- Development environments - testing programs for different platforms without having to use seperate devices. Saves time and money.

## Intermediate code
Languages like Java use intermediate VMs between the system and the source code. Code is compiled into **intermediate code or bytecode** and then a VM runs the code on the computer and translates it into machine code.

The same code can be run on any hardware device as long as it supports the virtual machine, making it highly portable

<img width="992" alt="Screenshot 2022-05-31 at 12 00 51" src="https://user-images.githubusercontent.com/72783315/171158867-a9776a77-76c0-491a-9d6b-0bef1a53a232.png">
