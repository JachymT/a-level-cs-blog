# Input, output and storage
## Keywords
Input device - allows data to be entered into a computer system for the CPU to process. This is needed to instruct the CPU to do something. For example a microphone, scanners, pressure sensors.

Output device - allows data to be transmitted from a computer system to a user. Data is usually formatted for the user to interact with. For example, a speaker, a door opening, a projector.

## Input and output examples
### Optical Character Recognition
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/1.png" height="100">
Takes images of shapes on a piece of paper and warps those shapes until OCR recognises that shape as a character on a database. Therefore it can take scanned documents and convert them to editable text files. Since pattern matching is a complicated process, OCR can make mistakes, but it is still faster than typing a document up by hand.

### Optical Mark Recognition
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/2.jpeg" height="100">
Used by exams and lottery systems for mass processing multiple choice questions. The OMR knows the predetermined form, and the questions position on the page, so it checks each area for a dark line, if most of the area is not covered, the result may be missed.

### Scanners
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/3.png" height="100">
Used for image digitisation, makes a bitmap from a flat piece of scanned media. Used in OCR and film scanning.

### Magnetic Ink Recognition
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/4.png" height="100">
Scans only for ink containing iron oxide, such as the account number on the bottom of cheques. More expensive method for scanning so rarely used but more reliable than OCR

### Barcodes
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/5.jpeg" height="100">
A storage device used on most products to uniquely identify them. Barcode readers can be used to look up that barcode on a database. Values are represented solely by the thickness of lines and their positions.

### Radio frequency identification (RFID)
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/6.png" height="100">
A passive technology for tracking an item. Uses tags and readers, the readers send radio waves and receive signals from a tag in return. Used in library books for example.

## Touch Screens
There are two main types of touch screens, capacitive and Resistive touch screens

[video explaning the differences](https://youtu.be/0-GQZzz_VTg)

### Capacitive touch screens
Takes advantage of conductivity of the human body. X and Y of a conductive pen or finger are recorded and send a precise signal. Can also have multiple points of contact, superior to resistive touch screens. Most touch screen phones, ipads and computer screens make use of this method.

### Resistive touch screens
Two sheets of transparent glass, when enough pressure is applied, the x and y coordinate is recorded from a voltage that is created. Less precise than capacitive but can be used with gloves so useful in a manufacturing environment.

## Sensors
Sensors record data from the physical environment, they are input devices.
Sensors record analog data, which needs to be converted to digital to be processed by the CPU

### Examples
- Temeperature (infrared) sensors
- Light(luminence) sensors
- pH sensors
- Pressure sensors
- Touch sensors
- Humidity sensors
- Colour sensors
- Sound sensors
- Proximity sensors
- Movement sensors

## Actuators
To iniciate physical movement, often an output as a result of a sensor. So they might pair with a sensor to open an automatic door

### Examples
- LED 

**Feedback loop**

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/7.png" height="500">

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
