# Character sets
Character sets are codes which can be recognised by the computer and are used to represent text / symbols / digits.**Character codes** are **unique bit-patterns**. A character set is simply a standardized set of bit patterns.

### ASCII 
ASCII uses 7 bits to represent numbers and symbols, and precedes Unicode.

### Unicode
Solves the problem of limited characters with ASCII, by using as many as 32bits (it uses a varying number of bits). The first 7 bits represent the same characters as ASCII and so it is backwards compatable. It allows for global communication.

# Binary

## Storing negatives in binary

### Sign and magnitude
Most Significant Bit (MSB is the left most bit) determines if the number is positive or negative, **1 signed negative, 0 signed positive**

No one cares :/

### Twos Compliment
Most Significant Bit is negative whatever it would ussually be. Flip all digits from left to right untill you reach the Least Significant 1 and keep it and the numbers after the same to change the sign. Basically flip everything left of the lowest 1 to swap sign.

Can be used in calculations as opposed to sign and magnitude. Standarised way to store negative numbers.

EXPONENT DOES NOT HAVE TO BE NORMALISED. You can't normalise -2 with 3 bits because theres no where to move them.

## Storing Floats/ Real numbers in binary

### Fixed point
Floating point without the exponent, useless in real life but in an exam they will tell you where the decimal is.

### Floating point
Exponent moves decimal to the right if positive and left if negative, starting from **after** the first digit in the mantissa. ( think of it as a literal exponent )

**mantissa x 2 ^ exponent**

## Normalisation
Maximising the precision of a number when storing it in a given number of bits. Denary numbers to normalised floating point binary numbers can be done in the following way.

![image](https://user-images.githubusercontent.com/72783315/157253704-b0537772-56ba-4de6-90bb-0f921a1babe7.png)

`011101 011`

for a positive number the mantissa **always starts with 01, and for a negative 10**. All leading 0s or 1s should be removed

Normalising binary floating points happens by moving the mantissa left or right and then changing the exponent acordingly. Moving decimal 3 **left increases** exponent by 3. moving decimal 3 **right decreases** exponent by 3.

## Adding floating points
1. Make any negative numbers into twos compliment form
2. Make all numbers into thier fixed point form
3. align the decimals ontop of each other and add as ussual, backfilling with 1s if negative and 0s if positive
4. For the last sum ignore the overflow digit, as it will carry on forever, also you can use intuition to determine if result will be positive or negative
5. Normalise the result: move decimal point after front 1 or 0 and set exponent

## Subtracting floating points
1. Make any negative numbers into twos compliment form
2. Just carry digits like with a normal subraction lol
   Or make one of them negative and add
3. Normalise the result

## Bitwise manipulations
Shifts can be logical or arithmetic or circular. Logical shifts fill empty space with 0s. Arithmetic shifts care about twos compliment numbers and fill with 1s if needed. Arithmetic preserve the sign bit! Circular use a carry bit and loop the number round. Since you dont loose information from doing a shift with a carry bit, you can keep shifting forever cyclically. Shifts are performed one after each other not all at once when shifting more than once.

The Carry bit stores the overflow bit. Can be used to check for the MSB or LSB. 

Left shifts multiply the number by powers of 2. Right shift divide the number by powers of 2 and truncate the answer.

## Bitwise Masks
Masks use boolean logic on binnary numbers. Imagine truth tables going across the whole number. They are used in networking to selects parks of the IP address that are needed for comparisons.

XOR is EXCLUSIVE OR, normal OR is inclusive. Only one can be true.

![image](https://user-images.githubusercontent.com/72783315/214966375-7404645b-a8b3-4684-bd8f-53cc51d50e3d.png)

An XOR bitwise mask flips the bits where its 1.

An AND bitwise mask clears (turns to 0s) the bits where its 0.

An OR bitwise mask fills (turns to 1s) the bits where its 1.
