# Networks
A network is any connection between two or more computers, and allows them to send data back and forth. Networks in a company allow for shared peripherals, files and backup resources.

A LAN is over a small geographical area. A LAN requires infastructure to be built, either with wi-fi or copper / fibre optic cables.

WAN is over a large geographical area or multiple locations. Infastructure is used from telecommunications companies (collective ownership), over telephone wires / satelites / chunky fibre optic cables.

![image](https://user-images.githubusercontent.com/72783315/195105764-dd6b8ffe-cfd5-4531-a56e-ed263db88396.png)

## Topologies
**Physical topologies** - How the wires are connected

**Logical topologies** - How the data flows

![image](https://user-images.githubusercontent.com/72783315/192552505-90d7a198-3280-4b83-b9fd-d1e2ea40bf0e.png)

### Bus Topology
Bus topology is litterally just a straight line. One cable, called the **backbone**, connects all the devices together.

**Advantages**
-

### Star Topology

### Mesh Topology

## The internet structure 
The internet is a network of networks allows for global communication between any connected devices.

### Protocols
A protocol is a set of rules for procesing data, standardized across the internet to allow for communication.
- HTTP / HTTPS - For web page requests
- TCP (Transmission Control Protocol) - error checks transmitions
- IP (Internet Protocol) - routes packets over WAN
- FTP (File Transmission Protocol) - Transmission of files over networks
- POP3 / IMAP / SMTP - For transfering emails between clients and servers

### TCP/IP Stack
Set of 4 network layers working together, in the following oder (top to bottom)

Application Layer - specifies what protocols needs to be used by the application (e.g a browser using HTTPS)

Transport Layer - establishes an end to end connection and splits data into packets, labled with the port number used and the packet number. The transport layer requests any packtets that get lost.

Network (internet) layer - Adds the source and destination IP addresss for each packet. The router operates on this layer using the IP protocol to route packets

Link Layer - connects devices through network hardware and data links. Connects to the destination MAC.

### Packet data
Packets are segments of data. They contain various information:

- Sender and recipient IP addresses - to deliver correctly and trace where it came from
- Protocol being used 
- Order of the packets
- Time To Live / Hop Limit - when it expires
- Actual data to be transmitted 
- Checksum - check for errors

A TCP/IP packet could contain:

![image](https://user-images.githubusercontent.com/72783315/195106282-db91910e-dda6-413a-b8d3-fd2da0fafeec.png)

## Hardware
Home networks ussually just put all of these into one device. Also A hub is just a faster switch. Fibreoptics / other cables exist

### Network Interface Card
Usually built into the motherboard, the NIC is needed for connecting to a network. Assigns a unique MAC address to the device

### Router
Allows for connection to other networks (the internet). Checks and moves packets

### Wireless Access Point
Allows Wi-Fi devices to connect to a wired network.

### Switch
Directs the flow of data in a Network, the centre of a network, and sends data to the individual devices.

### Cables
Fibre optic, Copper coaxel, 

### Network diagram
![image](https://user-images.githubusercontent.com/72783315/192541532-dc4173b3-ba3f-4954-8711-1ffe1a66f768.png)


## Client-server
A network where terminals (clients) connect to a central server. The server typically has lots of recourses and processing power. Clients inciates communication with the server and the server waits for client requests.

**Advantages**
- Secure - data is stored in one location
- central backups can be carreid out
- data and recoures can be shared between clients

**Disadvantages**
- single point of failure 0 if the server fails then the terminals fail
- expensive to set up
- proffesionals required to maintain the server

## Peer to Peer
A network where computers are connected together and can act as both servers and clients, both providing and requesting data.

**Advantages**
- cheap
- easy to maintain
- not dependent on a central server
- recourses can be shared between computers

**Disadvantages**
- backups must be performed seperatly
- imposible to trace the origins of files
- poor security
- hard to locate resources

## Security

### Firewall
Firewalls sits between a trusted and untrusted network, and prevent unauthorised access. A firewall limits access to the netwrok based on certain rules. 

These rules are called **packet filters** (or Access Control Lists), and the process is called **static filtering**. Traffic is controlled by loking at the packet headers - IP address, destination IP address, port number and protocol used. If the port is closed anyway, or the firewall decided to not let the packet through, then the packet is either silently dropped, or rejected and a notification is sent back to the sender.

A more secure version of this is called **statefull inspection**, this just keeps track of all connections established, and checks what the packets contain.

### Proxy
Proxies act as an intermediary server between the client and the firewall, and sends out data on thier behalf.

They provide additional security by:
- **providing anonymity** because the client IP address cannot be directly seen
- **speeding up access** because it keeps a cache of frequently visited web pages
- **reducing web trafic** because it keeps a cache of frequently visited web pages
- **adding web filtering** because administrators for a network can add filters to prevent viewing sensitive content

### Encryption
Makes sure data sent is unreadable if intercepted. Encrypted and decrypted using keys and is using symmetrical or asymmetrical. Wireless security encrypts using either WEP, WPA, or WPA2.

### Malicous software
Worms are stand alone and self replicating. Viruses infect other programs or data files with the users help.

### Prevention
Update patches to the operating system and application programs reduce vulnerabilities in the system. 

Update anti-malware (“anti-virus”) software can prevent the spread of infection
