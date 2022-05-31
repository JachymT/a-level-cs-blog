# Basic Input Output System

The BIOS is a program stored in a non-volatile ROM chip and is in charge of performing checks before the OS can be loaded. The BIOS is read only and so configurable settings are stored in a CMOS chip, which has its own battery. The CMOS also keeps track of the time with a permanent clock.



## When a computer first turns on
The BIOS runs on Start up:

1. Performs the **POST** (power on self test) to check all hardware devices are connected and functional
2. Checks CPU clock, memory and processor are all working
3. Tests for external memory devices connected to the computer
4. Loads the **bootstrap** from the hard disk into main memory. This initialises the Operating System.

Without BIOS, the computer would not be able to start as nothing is loaded in RAM
