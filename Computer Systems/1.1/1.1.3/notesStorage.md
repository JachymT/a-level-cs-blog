# Storage
Binary computers mean that storage can take advantage of the speed that it takes to detect one of two states. E.g magnetic storage uses magnetic polarity and SSDs use floating gate transistors.

## RAM
Random access memory - Fast, **temporary** and **volite** memory. RAM compunicates back and forth with the CPU by buses, and information stored in RAM is processed by the CPU. Since its close to the CPU its much faster than accessing secondary storage (hard disk). RAM is fast because moving between secondary and primary storage is slow and more RAM reduces the need for virtual storage.

The RAM holds the operting system while the computer is running along with other programs.

Similar to flash memrory but has the difference of volility.

## ROM
Read only memory - **Non volitile**, read only memory that stores a small part of the Operating system called the **POST**, **bootstrap** and **BIOS**. It initializes the system hardware and then boots up the operating system, as part of the first thing at happens when you boot up the computer. 

The initial instructions ROM opens are called the **bootstrap**, followed by the software on ROM, called **firmware**. After this a **power-on self test (POST)** is done. This tells connected components to wake up and tells the CPU that they exist. Now the CPU can move the operating system from the hard drive to RAM.

Some ROMs can be changed for examples cartridges in a DS, but most are soldered on to the motherboard.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/RamRomDifferences.PNG" height="500">

## Optical storage
Optical media includes Compact Disks (CDs), Digital Versitile Disks (DVDs) and Blue-rays. 

### How they work
Optical drives work by **lazers** being shined on the drive and the **reflected** or **scattered** light being processed. The surface of a disk has **pits and lands** which reflect the laser differently and so can store binary data. They are read-only and have to be pressed or burned with data.

### Positives
 - Popular for distributing music and movies, mostly because of thier ease of distribution. 
 - They are **cheap, lightweight and portable**
 - Sometimes can be used for backups

### Negatives
 - Slow access times - read from the inside to the outside. 
 - Not durability - prone to scratches.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/stor1.PNG" height="200">

## Magnetic storage
Typical Hard disks and tape use magnetic media.

### How they work
Very small magnetic components represent binary data, being in one of two states: **polarised and unpolarised**. A **drive head** phyically moves over a disk, and reads a 1 or a 0 depending on if the magnetic poles in the drive head align or not. The platters mechanically spin at high speeds and magnetic patterns are read

### Positives
 - Very **high capacity** - between 500GB and 5TB.
 - Cheap
 - Still often used for backups but largely superseded by sold state and cloud storage.

### Negatives
 - It will eventually fail, low durability.
 - Slow access times because it has moving parts, even though the drive head moves very fast

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/stor2a.PNG" height="200">

## Solid state storage
Typical SSDs use flash media. Other examples include USB sticks and flash memory cards (eg. SD cards).

### How they work
Work by flowing electricity forcing electrons into a floating gate between two oxide layers. This causes a change of charge in the floating gate - if a charge is trapped a 1 is messured and if not a 0.  NAND gates form each of the memory cells.

### Positives
 - Small, lightweight and portable - **compact**
 - Very quick to access - **fast**
 - silent
 - Large capacity
 
### Negatives
 - Oxide layers will eventually deteriorate - limited read/writes
 - Costly but getting cheaper

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/stor3.PNG" height="200">

## Virtual storage
Storing information remotely so that it can be accessed by any computer with access to the same system, for example over the Internet, or over cloud storage services like google drive and networked storage used in schools.

### How it works
Virtual storage is often an abstraction of multiple drives acting like one. Information stored in the cloud is actually stored on 100s of hard drives or SSDs formatted to act as a single piece of storage - in large **data centres** owned by the companies providing the cloud storage.

### Positive
 - **Remote** - can be accessed anywhere conviently
 - Can have **unlimited capacity**
 - Can easily be shared between devices

### Negatives
 - Limited to a users network access and speed
 - Often high cost

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/stor4.PNG" height="200">

_Images from https://www.youtube.com/watch?v=yhDmlhc_2_M and https://www.youtube.com/watch?v=zzyCGHfuqe8_
