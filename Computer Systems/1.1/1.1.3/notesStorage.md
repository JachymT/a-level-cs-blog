# Storage
## RAM
Random access memory - Fast, temporary and volite memory, often flash memory. RAM compunicates back and forth with the CPU by buses, and information stored in RAM is processed. Since its close to the CPU its much faster than accessing secondary storage (hard disk). 

The RAM holds the operting system while the computer is running.


## ROM
Read only memory - Non volitile, read only memory that stores a small part of the Operating system called the POST, bootstrap and BIOS. It initiazles the system hardware and then boots up the operating system, as part of the first thing at happens when you boot up the computer. 

The initial instructions ROM stores are called the **bootstrap** and the software on ROM is called firmware. After this a **power-on self test (POST)** is done. This tells connected components to wake up and tells the CPU that they exist. Now the CPU can move the operating system from the hard drive to RAM.

Some ROMs can be changed for examples cartridges in a DS, but most are soldered on to the motherboard.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/RamRomDifferences.PNG" height="500">

## Optical storage
Optical media includes Compact Disks (CDs), Digital Versitile Disks (DVDs) and Blue-rays. 

### How they work
Optical drives work by lazers being shined on the drive and processing the reflection. The surface of a disk has pits and lands which reflect the laser differently and so can store binary data. They are read-only and have to be pressed or burned with data.

### Positives
 - Popular for distributing music and movies, mostly because of thier ease of distribution. 
 - They are **cheap, lightweight and portable**
 - Sometimes can be used for backups

### Negatives
 - Slow access times - read from the inside to the outside. 
 - Not durability - prone to scratches.

## Magnetic storage
Typical Hard disks and tape use magnetic media.

### How they work
Very small magnetic components represent binary data. A drive head phyically moves over a disk.

### Positives
 - Very high capacity. 
 - Still often used for backups but largely superseded by sold state and cloud storage.

### Negatives
 - It will eventually fail, low durability.
 - Slow access times because it has moving parts.

## Solid state storage
Typical SSDs use magnetic media. Other examples include USB sticks and flash memory cards (eg. SD cards)

### How they work
Work by flowing electricity forcing electrons into a floating gate between two oxide layers. This causes a change of charge in the floating gate, which can be messured as a 1 or 0, in oder to store binary data

### Positives
 - Small, lightweight and portable
 - Very quick to access
 - silent
 - Large capacity
 
### Negatives
 - Oxide layers will eventually deteriorate - limited read/writes
 - Costly but getting cheaper

## Virtual storage
Storing information remotely so that it can be accessed by any computer with access to the same system, for example over the Internet, or over cloud storage services like google drive and networked storage used in schools.

### How it works
Virtual storage is often an abstraction of multiple drives acting like one. Information stored in the cloud is actually stored on 100s of hard drives or SSDs formatted to act as a single piece of storage. 

### Positive
 - Convinient - can be accessed anywhere
 - Can have unlimited capacity

### Negatives
 - Limited to a users network access and speed
 - Often high cost
