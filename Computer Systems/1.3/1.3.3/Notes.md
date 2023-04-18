# Networks
A network is any connection between two or more computers, and allows them to send data back and forth. Networks in a company allow for shared peripherals and files, and for remote backups and maintenance.

A LAN is over a small geographical area. A LAN requires infastructure to be built, either with wi-fi or copper / fibre optic cables.

WAN is over a large geographical area or multiple locations. Infastructure is used from telecommunications companies (collective ownership), over telephone wires / satelites / chunky fibre optic cables.

![image](https://user-images.githubusercontent.com/72783315/195105764-dd6b8ffe-cfd5-4531-a56e-ed263db88396.png)

## Topologies
**Physical topologies** - How the wires are connected. Devices attached can be called nodes, terminals, station or whatever you want, no one cares.

**Logical topologies** - How the data flows

![image](https://user-images.githubusercontent.com/72783315/192552505-90d7a198-3280-4b83-b9fd-d1e2ea40bf0e.png)

### Bus Topology
Bus topology is litterally just a straight line. One cable, called the **backbone**, connects all the devices together. 

**Advantages**
- cheap
- no extra hardware required

**Disadvantages**
- If backbone cable fails, the entire network fails
- As traffic increases, performance decreases
- All computers can see the data transmission

### Star Topology
Connect to central node (often a switch). MAC addresses identify each device.

**Advantages**
- If one cable fails, only that single node is affected
- better performance and data transmission than bus topology
- Easy to add new nodes
- No data collisions

**Disadvantages**
- Relies on a central switch
- cabling and switch are expensive

### Mesh Topology
All nodes connected. Wifi is a mesh.

**Advantages**
- If using a wireless network, there is no cabling cost
- The more nodes the more reliable (which is how wifi works)
- Fastest 

**Disadvantages**
- If using a wireless network, devices must have wireless capability
- If using a wired network, lots of cables needed, which is expensive
- Maintaining the network is difficult

## Internet structure 
The internet is a network of networks allows for global communication between any connected devices.

### Protocols
A protocol is a set of rules for procesing data, standardized across the internet to allow for communication.
- HTTP / HTTPS - For web page requests
- TCP (Transmission Control Protocol) - Error checks transmitions, splits into packets
- IP (Internet Protocol) - Routes packets over WAN
- FTP (File Transmission Protocol) - Transmission of files over networks
- POP3 / IMAP / SMTP - For transfering emails between clients and servers

### TCP/IP Stack
Set of 4 network layers working together, in the following oder (top to bottom)

Application Layer - specifies what protocols needs to be used by the application (e.g a browser using HTTPS)

Transport Layer - establishes an end to end connection and splits data into packets, labled with the port number used and the packet number. The transport layer requests any packets that get lost.

Network (internet) layer - Adds the source and destination IP addresss for each packet. The router operates on this layer using the IP protocol to route packets

Link Layer - connects devices through network hardware and data links. Connects to the destination MAC.

![image](https://user-images.githubusercontent.com/72783315/196445137-b1aba957-4267-4493-b6d1-1ba2d6d27225.png)

## Packet data
Packets are segments of data. They contain various information:

**Header**
- Sender IP addresses - to deliver correctly 
- Recipient IP addresses - to trace where it came from
- Protocol being used 
- Order of the packets
- Total number of packets in the file
- Time To Live / Hop Limit - when it expires

**Main body + tail**
- Actual data to be transmitted (packets are equally sized ussually idk)
- Checksum - check for errors

A TCP/IP packet could contain:

![image](https://user-images.githubusercontent.com/72783315/195106282-db91910e-dda6-413a-b8d3-fd2da0fafeec.png)

## Network Switching
netweork switching is sending data to some hardware component.

### Packet switching
One method of packet switching is packet switching. Data is sent over networks in small chunks called data packets / ip packets. Packets are treated individualy and can travel across any route. Routers are responsible for directing packets along the best route. For example if a router fails the packts just go around it. At the destination the packets are assembled and any missing packets are requested. 

The header of the packet contains information that the routers need for packet switching (see above).

### Network Switching

https://teachcomputerscience.com/packet-and-circuit-switching/
https://teachcomputerscience.com/packet-and-circuit-switching/
https://teachcomputerscience.com/packet-and-circuit-switching/
https://teachcomputerscience.com/packet-and-circuit-switching/https://teachcomputerscience.com/packet-and-circuit-switching/https://teachcomputerscience.com/packet-and-circuit-switching/https://teachcomputerscience.com/packet-and-circuit-switching/

https://teachcomputerscience.com/packet-and-circuit-switching/

### Network Performace
Network traffic causes latency - packets build up in the switch / routers memory and take longer to arrive. Latency (delay), error rate (how many packets get lost) and bandwidth (speed of transfer - affected by the transmission medium, e.g. fibreoptic cable.) all affect network performance.

## Hardware
Home networks ussually just put all of these into one device. Also a switch is just a faster hub. Fibreoptics / other cables exist.

### Network Interface Card
Usually built into the motherboard, the NIC is needed for connecting to a network. Assigns a unique MAC address to the device

### Router
Allows for connection to other networks (the internet). Checks, sends and recieves packets meaningfully to reduce traffic.

### Gateway
A gateway is the same as router, except it sends and recieves data between unfamilar / different types of networks. Unlike routers they can also operate at any layer of the TCP/IP stack and use any protocol. A gateway can also translate between protocols and so it is used to make sure that networksthat have thier own protocols in place can communicate with the Internet.

Gateways can also be used as proxy servers or firewalls.

### Wireless Access Point
Allows Wi-Fi devices to connect to a wired network.

### Switch
Connects devices together Directs the flow of data in a Network, the centre of a network, and sends data to the individual devices.

### Cables
Fibre optic, Copper coaxel (cheaper, slower)

### Bridge
Larger networks can be broken down into smaller networks and these are connected together using a Bridge. This can improve performance as each section has its own bandwidth. Usefull for splitting up / joing together a school network. Works at the data link layer.

### Network diagram
<img src="https://user-images.githubusercontent.com/72783315/192541532-dc4173b3-ba3f-4954-8711-1ffe1a66f768.png" height="350">

## Client-server
A network where terminals (clients) connect to a central server. The server typically has lots of recourses and processing power. Clients inciates communication with the server and the server waits for client requests. Uses dedicated servers

**Advantages**
- Secure - data is stored in one location
- central backups can be carreid out
- Shared resources - files and peripherals can be accessed by clients

**Disadvantages**
- single point of failure, if the server fails then the terminals fail
- expensive to set up
- proffesionals required to maintain the server

## Peer to Peer
A network where computers are connected together and can act as both servers and clients, both providing and requesting data.

**Advantages**
- cheaper
- easy to maintain
- not dependent on a central server
- recourses can be shared between computers

**Disadvantages**
- backups must be performed seperatly
- imposible to trace the origins of files
- poor security
- hard to locate resources

Both architectures form a network and allow for sharing files and data

<img src="https://user-images.githubusercontent.com/72783315/196441612-385bab50-92bb-4a87-9f90-e95c8e4579c7.png" height="350">

## Security

### Firewalls
Firewalls sits between a trusted and untrusted network, and prevent unauthorised access. A firewall limits access to the netwrok based on certain rules. TLDR: Malicious packets trying to access forbidden ports are rejected. 

These rules are called **packet filters** (or Access Control Lists), and the process is called **static filtering**. Traffic is controlled by loking at the packet headers - IP address, destination IP address, port number and protocol used. If the port is closed anyway, or the firewall decided to not let the packet through, then the packet is either silently dropped, or rejected and a notification is sent back to the sender. 

A more secure version of this is called **statefull inspection**, this just keeps track of all connections established, and checks what the packets contain.

### Proxies
Proxies act as an intermediary server between the client and the firewall, and sends out data on thier behalf.

They provide additional security by:
- **providing anonymity** because the client IP address cannot be directly seen
- **speeding up access** because it keeps a cache of frequently visited web pages
- **reducing web trafic** because it keeps a cache of frequently visited web pages
- **adding web filtering** because administrators for a network can add filters to prevent viewing sensitive content
- **keeps user logs** 

### Encryption
Makes sure data sent is unreadable if intercepted. Encrypted and decrypted using keys and is using symmetrical or asymmetrical. Wireless security encrypts using either WEP, WPA, or WPA2.

### Authentications
Authentication in a network is basically user access levels. Require a username and password to log on, with multiple redentials (normal, admin). Done through the use of Smart cards and biometrics (fingerprints).

### Prevention
- 4 things above
- Updating the operating system and application programs reduce vulnerabilities in the system. 
- Updating / Installing anti-malware (“anti-virus”) software
- Have unique, complex passwords
- Don't click on phishing links

### Malicous software
- Worms are self executing and self replicating. 
- Viruses are self executing and infect other programs or data files with the users help.
- A Trojan requires user help to install and cannot self-replicate.
