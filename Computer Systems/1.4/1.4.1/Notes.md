# Binary

## Storing negatives in binary

### Sign and magnitude
Most Significant Bit (MSB is the left most bit) determines if the number is positive or negative, **1 signed negative, 0 signed positive**

### Twos Compliment
Most Significant Bit is negative whatever it would ussually be. This way we have to flip all digits from left to right untill you reach the last 1 and you keep it and the numbers after the same. 

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
