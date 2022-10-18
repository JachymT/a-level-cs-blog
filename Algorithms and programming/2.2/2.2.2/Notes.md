# Computational Methods
For solving problems of a computational nature. The problem must be:
- Solved within a finite amount of time
- Have inputs outputs and calculations 
- clearly defined
- considered if decomposition and abstraction are possible to apply
- considered what storage is needed and what data is being handled

## Visualisation
Visualistation can be any process that represents data or a problem, often in an illustrative way. Images and graphs help people solve complex tasks or understand models. For example drawing a diagram for an algorithm isntead of reading pseudocode.

Need to consider what form works best to avoid being innaccurate (e.g using MAT LAB for th), but it should still be simplistic and focus on the most important and clear data.

Examples
- https://visme.co/blog/best-data-visualizations/
- https://www.101computing.net/data-visualisation-algorithms/


## Performance modelling
Performance modelling (testing) evaluates a model's performance and uses that knowledge to improve it. It does this by approxmiating using aproximations and simulations. Mathematical tests, rather than in feild test, reduce costs, time and safety risks.

Provides a cheaper and easier method of testing, since it can be done before the final system is fully implemented (or using a scaled down or hypothetical version of the system). This means the results can also be monitered more closely, rather than testing thousands of connections at once. Image a plane.

Stress testing can be done to test ‘erroneous’ scenarios of the program.

The aim is to know how well the full implementation of the solution will work before release.

## Heuristics
Heuristics is finding a solution that is good enough when an optimal solution is unknown or impossible. Using approximate solutions to problems that aren't computational (infinite time solutions), to get as close as possible to an efficient solution. Heuristics can be done with modelling.

Example: Travelling Salesman Problem as well as the A* algorithm.

## Data Mining
Data mining is used for identifying patterns in large sets of data. Reveals underlying trends and relationships. Mining large data sets is costly on resources and processing power.

Examples are: Neural networks, statistics and data science.

## Pipelining
Pipelinig Breaks down a process into a series of subtasks. Output of one task feeds into the input of another task. Subtasks are dependent on each other, which can be a disadavantage. Pipelining also happens in multi core processors when using parallel processing (kind of idk, might be the same thing).

Examples are: Blocked, running and waiting states in a processor queue.

## Backtracking
Backtracking is used to move between options in a problem, going down decision routes. It works by backtracking if you reach a dead end to the last decision made. Uses recursive methods, and will methodically find all valid  / invalid options. Recursion, however, is slow for large problems.

Examples: Recursive algorithms (eg. going through a maze, finding shortest paths, or the best option in a chess game). Also depth first traversal
