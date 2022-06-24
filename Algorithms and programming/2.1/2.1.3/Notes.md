# Thinking procedurally
Thinking procedurally makes writing programs easier by problem decomposition making it easier to design and partition. A large and complex problem is broken down in smaller, underlying subproblems that need to be solved.

## Top-down design (hierarchy chart)
Known as **stepwise refinement**, tasks are split into smaller tasks, in a modular structure. Higher up levels provide an overview while lower down levels specify details about the program. Ideally each subroutine at the bottom (the lowest level componenets)(in the diagram level 2 is the lowest idk why) are self-contained and independent. Finnally all components are combined into one solution, by turning each task into a function with its own parameters

![image](https://user-images.githubusercontent.com/72783315/174592312-e71823d8-dbf8-4fb4-b04f-fd4bc881c718.png)

## Advantages
- Independent modules can be tested seperately
- Makes it easier to identify a solution to the problem
- Existing modules or libraries can be used to reduce complexity
- Saves time and money as modules can be repeated
- Increases maintainability and readability

## Disadvantages
- Need to consider how modules interact with each other
- And order of execution (such as getting inputs first)
