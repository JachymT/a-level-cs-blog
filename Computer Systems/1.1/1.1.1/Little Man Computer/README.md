# Solutions

## Part 1
### Task 1
INP
STA 99
INP 
STA 98
INP
OUT
LDA 98
OUT
LDA 99
OUT
HLT

### Task 2
INP
STA 99
INP 
ADD 99
STA 99
INP
ADD 99
OUT
HLT

### Task 3
INP
STR first
ADD first
OUT
HLT
first DAT

### Task 4
INP
STA first
INP
STA second
LDA first
SUB second
OUT
LDA second
SUB first
OUT
HLT
First DAT
Second DAT

## Part 2
### Task 1
INP 
STA a
INP
STA b
SUB a
BRP Last
LDA a
OUT
HLT
Last LDA b
OUT
a DAT
b DAT

### Task 2
INP
STA a
INP
STA b
SUB a
BRZ Last
LDA a
ADD b
OUT
Last OUT
HLT
a DAT
b DAT

### Task 3
INP 
STA a
INP
STA b
LDA a
Loop SUB b
BRZ End
BRP Loop
End OUT
HLT
a DAT
b DAT
