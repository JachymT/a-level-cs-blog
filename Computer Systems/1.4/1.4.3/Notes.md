# Boolean Algebra

![image](https://user-images.githubusercontent.com/72783315/221139813-cfad7c45-3936-4a72-b768-f18b533540a6.png)

![image](https://user-images.githubusercontent.com/72783315/221140764-a802ac9e-f70d-49ea-8810-21bb95094554.png)

### Imporant ones (all the do with a something being done to a single backet)
- De Morgan's law: to exapnd a negative bracket flip the operator.  ¬ (A ∧ ¬B) -> ¬A ∨ B
- Distribution: expand backets between ANDs and OR and add backets to the pairs. A ∨ (B ∧ C) -> (A ∨ B) ∧ (A ∨ C)
- Absoption when the operators are different and the letter outside is the same as one of the inside ones you can simplify to just the outside one. A ∧ (A ∨ ¬B) -> A

## Logic circuits

### Half Adder
Adds two binnary numbers with a XOR for the sum and an AND for the carry

<img width="500" alt="1" src="https://user-images.githubusercontent.com/72783315/222000113-d097c9b1-2908-42f6-820d-a814b8045240.png">

### Full Adder
Adders can be concatenated to get multiple additions, just add an OR to the last carry

<img width="500" alt="2" src="https://user-images.githubusercontent.com/72783315/222000813-52c8fa20-fa64-45db-af3b-f6d18f6c1da7.png">

### Flip Flops

A clocked D latch (D type flip flop) controls the state of a single bit. They make up memory, such as registers and RAM.

<img width="200" alt="3" src="https://user-images.githubusercontent.com/72783315/222006322-a60c231e-3fbb-4401-8ee5-e4571c514f71.png">

Flip flops take the value to be stored as an input and a clock signal (alternative at regular intervals). The type of D type type flip flop determines how the clock is used. Most commonly the edge of the the clock signal changing is used as an input in the circuit, so every time the signal goes from 0 to 1, a 1 is instanly used to store the current value of D.

<img width="500" alt="4" src="https://user-images.githubusercontent.com/72783315/222006325-86109fcc-d3d5-43aa-ba63-b97e042e5af2.png">

## Karnaugh maps

∧ AND

∨ OR

⊻ XOR

¬ NOT

() do operations inside brackets first. order of operations normally is to do the operatiosn around ORs first. Put brackets around anything which isnt a OR, basically just do ANDs first and it works.

Groups inside Karnaugh maps must cover all 1s. Group rectangles in sizes of 1, 2, 4, 8 ... 2^n. Groups can overlap, wrap around and should be made in as few rectangles as possible. These can then be used to simplify the expression, which makes it easier to read and requires less physical hardware to make on a circuit board. Prioritise larger groups even if that means they overlap, basically make the largest groups you can.

![image](https://user-images.githubusercontent.com/72783315/221143287-b06a5d28-aa5e-4b02-8f77-9b5c3a1f16c4.png)
