# Investigate the factors affecting the performace of the CPU

## Clock speed
Clock speed or rate is the frequency at which the CPU can generate 

## Number of cores
A core is an independent processor that can run its fetch-decode-execute cycle. A CPU have dual-core, quad-core or more processors. The CPU can co-ordinate the cores and so uses them together to 

This theoretically allows for 2x, 4x or more times as many instructions executed per second. However all cores can not always be utilized efficiently, and cores comunicating becomes more complicated and uses processing power. They are particularly useful for multitasking, and since computers are nearly always mulitasking, so there is a large benefit compared to having a single core processor.

## Cache
Cache is CPU's on board memory, where some. It the **closest and fastest** memory for storing instructions, which are copied over from RAM. Less frequently used instructions in cache are replaced with more commenly fetched ones. The CPU checks for cache before checking RAM.

![image](https://user-images.githubusercontent.com/72783315/136964131-995ef064-440c-4701-be76-4a435ec3a677.png)
_[image from](https://developer.arm.com/documentation/den0024/a/Caches)_

Faster and more cache increase the CPU's performance since instructions are being storied closer. There are restrictions on Cache usage however and most modern processor have 128KB to 8MB of Cache memory, which is divided into levels. Cache is effient when it is fast to fetch from so a large cache would be detrimental, since the CPU has to check much many more location each time. Levels of Cache help further maximise efficiny, level 1 is closest to the CPU and smallest, going up to level 3 where they get larger and take longer to fetch from.

Cache is also much more expensive than other memory.

## Conclusion
Fundementally

_references_
- [pmt.physicsandmathstutor.com](https://pmt.physicsandmathstutor.com/download/Computer-Science/A-level/Notes/OCR/1.1-Characteristics-of-Contemporary-Processors-Input-Output-and-Storage-Devices/Intermediate/1.1.1.%20Structure%20and%20Function%20of%20the%20Processor.pdf)
- [isaaccomputerscience.org](https://isaaccomputerscience.org/concepts/gcse_sys_cpu_performance?examBoard=all&stage=all&topic=gcse_systems)
