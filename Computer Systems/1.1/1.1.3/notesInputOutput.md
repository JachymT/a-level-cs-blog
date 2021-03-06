# Inputs and outputs
## Keywords
Input device - allows data to be entered into a computer system for the CPU to process. This is needed to instruct the CPU to do something. For example a microphone, scanners, pressure sensors.

Output device - allows data to be transmitted out from a computer system. Data is usually formatted for the user to interact with. For example, a speaker, a door opening, a projector.

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
- Altimeter - when the wearer is ascending / descending
- Accelerometer - measure forces on device when it moves
- Gyroscope - measures if wearer turns

## Actuators
Used to iniciate physical movement, often an output as a result of a sensor. So they might pair with a sensor to open an automatic door. 

### Examples
- Electric motors
- pistons
- pumps
- digital camera lenses

**Feedback loop**

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.1/1.1.3/images/7.png" height="500">
