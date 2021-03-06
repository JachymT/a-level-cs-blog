# Investigate the factors affecting the performace of the CPU

*16 mark essay awnser to a CPU performace question*

*In the exam be specific and relate to the question senario*

## Clock speed
Clock speed or rate is the frequency at which the CPU clock can generate pulses. These pulses are electrical signals that synchronize operations inside the CPU. With each tick another cycle passes, so the more ticks per second the more instructions perfomed per second, so programs are run faster.

Clock speed is messured in Hz, with a typical CPU messuring 3.5 GHz = 3.5 billion instructions per second.

## Number of cores
A core is an independent processor that can run its fetch-decode-execute cycle. A CPU have dual-core, quad-core or more processors. The CPU can co-ordinate the cores - using them together.

This theoretically allows for 2x, 4x or more times as many instructions executed per second. However all cores can not always be utilized efficiently, and cores comunicating becomes more complicated and uses processing power. They are particularly useful for multitasking, and since computers are nearly always mulitasking, so there is a large benefit compared to having a single core processor.

Programs designed to do **parallel processing** benifit greatly from multiple cores.

## Cache
Cache is CPU's on board memory, it is Random Access memory but either in or next to the CPU. It the **closest and fastest** memory for storing instructions, which are copied over from RAM. Less frequently used instructions in cache are replaced with more commenly fetched ones. The CPU checks for cache before checking RAM.

![image](https://user-images.githubusercontent.com/72783315/136964131-995ef064-440c-4701-be76-4a435ec3a677.png)

_[image from developer.arm](https://developer.arm.com/documentation/den0024/a/Caches)_

Faster and more cache increases the CPU's performance since instructions are being storied closer and RAM is accessed less frequently. There are restrictions on Cache usage however and most modern processor have 128KB to 8MB of Cache memory, which is divided into levels. Cache is effient when it is fast to fetch from so large cache would be detrimental, since the CPU has to check many more locations each time. Levels of Cache help further maximise efficiency, level 1 is closest to the CPU and smallest and fastest (2-64KB), going up to level 3 where they get larger and take longer to fetch from.

Cache is also much more expensive than other memory.

## Conclusion
Fundementally a high clock speed in most important in the CPU since the more instructions that can be perfomed per second in a CPU the faster it will be at running programs. Clock speed is always benefitial, and while more cache and cores are useful for high end processing like renderign 3d graphics, they might not always be benfitial. However without efficient cache, freqeunt instructions will take hundrends of times longer to fetch. More cores, when utilized effciently, can provide many more times the processing power. Both more cach and cores come at a large price at the end of the performance curve.

### references
- [pmt.physicsandmathstutor.com](https://pmt.physicsandmathstutor.com/download/Computer-Science/A-level/Notes/OCR/1.1-Characteristics-of-Contemporary-Processors-Input-Output-and-Storage-Devices/Intermediate/1.1.1.%20Structure%20and%20Function%20of%20the%20Processor.pdf)
- [isaaccomputerscience.org](https://isaaccomputerscience.org/concepts/gcse_sys_cpu_performance?examBoard=all&stage=all&topic=gcse_systems)
- [wikipedia](https://en.wikipedia.org/wiki/Clock_rate)
- [gradeacomputerscience.com](https://gradeacomputerscience.com/what-factors-affect-cpu-performance)
