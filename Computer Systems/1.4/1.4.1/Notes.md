# Character sets
Character sets are codes which can be recognised by the computer and are used to represent text / symbols / digits.**Character codes** are **unique bit-patterns**. A character set is simply a standardized set of bit patterns.

### ASCII 
ASCII uses 7 bits to represent numbers and symbols, and precedes Unicode.

### Unicode
Solves the problem of limited characters with ASCII, by using as many as 32bits (it uses a varying number of bits). The first 7 bits represent the same characters as ASCII and so it is backwards compatable. It alows for global communication.

# Binary

## Storing negatives in binary

### Sign and magnitude
Most Significant Bit (MSB is the left most bit) determines if the number is positive or negative, **1 signed negative, 0 signed positive**

### Twos Compliment
Most Significant Bit is negative whatever it would ussually be. Flip all digits from left to right untill you reach the Least Significant 1 and you keep it and the numbers after the same to change the sign

Can be used in calculations as opposed tp sigh and magnitude. Standarised way to store negative numbers.

## Storing Floats/ Real numbers in binary

### Fixed point
Floating point without the exponent, useless in real life but in an exam they will tell you where the decimal is

### Floating point
Exponent moves decimal to the right if positive and left if negative, starting from after the first digit in the mantissa.

**mantissa x 2 ^ exponent**

## Normalisation
Maximising the precision of a number when storing it in a given number of bits. Denary numbers to normalised floating point binary numbers can be done in the following way

![image](https://user-images.githubusercontent.com/72783315/157253704-b0537772-56ba-4de6-90bb-0f921a1babe7.png)

`011101 011`

for a positive number the mantissa **always starts with 01, and for a negative 10**. All leading 0s or 1s should be removed

Normalising binary floating points happens by moving the mantissa left or right and then changing the exponent acordingly. Moving decimal 3 **left increases** exponent by 3. moving decimal 3 **right decreases** exponent by 3.

## Adding floating points
1. Make any negative numbers into twos compliment form
2. Make all numbers into thier fixed point form
3. align the decimals ontop of each other and add as ussual, backfilling with 1s if negative and 0s if positive
4. For the last sum ignore the overflow digit, as it will carry on forever, also you can use intuition to determine if result will be positive or negative
5. Normalise the result: move decdimal point after front 1 or 0 and set exponent

## Workings from Positive Binary and Hexadecimal Integers - Workbook.docx
*page 12*

```
1. a. 1100 + 101010 = 110110
   b. 100000 + 10010 = 110010
   c. 1100110 + 10101 = 1111011
   d. 10000001 + 110000 = 10110000
   e. 10110101 + 110011 = 11101000
   
2. a. 151 - 108 = 101011
   b. 127 - 56 = 1000111
   c. 241 - 153 = 1011000
   d. 143 - 120 = 10111
   e. 224 - 184 = 101000
(denary sums to binary)

3. 64 bits = 2^64 possible values = 1.8446744e+19 = 18446744073709551616

4. a. 10010101 = 95
   b. 01111100 = 7C
   c. 01010110 = 56
   d. 11110111 = F7
   e. 11001110 = CE
   
5. a. 52 - 19 = 21
   b. 66 - 35 = 1F
   c. 71 - 50 = 15
   d. 164 - 88 = 4C
   e. 187 - 66 = 79
(denary sum to hex)
```
   
**Explain why the hexadecmial number system is used**

It is simpler representation of binary, so binary can be processsed easier without noting all the digits.
It converts easier to binary than denary does, since 4 binary digits compile to one hex digit.

## Workings from Datatype practise Exam questions pdf

```
1. a. 0100.11 = 4.75
   b. -5.25 = - 0101.01 
      = 1010.11
      moving decimal 3 left, exponent = 011
      1010 011
   c. 0101 1110 = 5e
   d. 87 = 64 32 16 8 4 2 1
            1  0  1 1 0 0 1
      -87 = 10100111
   e.  01001001
      +11010001
      ---------
       00011010
      ---------
      11     1
   f. 9B = 9x16 + 11x1 = 144 + 11 = 155
   
3. a. i. -89 = 128 64 32 16 8 4 2 1
               - 0  1  0  1 1 0 0 1
             = 10100111
      ii.-72 = - 0  1  0  0 1 0 0 0
             = 10111000
   b.  10100111
      +10111000
      ---------
       01011111
      ---------
      1 1
   c. overflow
4. a. +/-  64 32 16 8 4 2 1
        1   1  1  1 0 1 1 1
        
   b. -128 64 32 16 8 4 2 1
         1  0  0  0 1 0 0 1
         
5. a. 0111 001
   b. exponent = -1
      0.011 = 3/8
```
