# Information

Thank you for taking this challenge! [CS Games](https://2020.csgames.org/) is an event that the [Computer Science Society](https://css.uwindsor.ca) sponsors annually. We send two teams of ten students (20 total) to compete in a series of competitions and have a great time. You are currently taking the challenge for our **Team A**, which is for students in 3rd/4th year. **If you're in 1st or 2nd year this challenge is not mandatory**, however your solution to this will be used when considering you for Team B.

This year we're combining a technical question with the GitHub platform so that we know you have some basic git knowledge. A lot of the CS Games competitions require git knowledge to submit your solutions.

Your final submission must be **pushed to this repository** by **November 30th at 11:59pm.** Be sure to also complete the application form!

# Grading

Your solutions will be tested with many test cases. We will look at algorithm correctness against these test cases as well as time complexity when assessing your solution.

# Submitting

Push your solutions to this repository on the master branch. You may use any programming language of your choosing. Please save the file that we should run as a file named `solution` (e.g. `solution.py`, `solution.c`).

# Question

Given a two-dimensional grid of letters and a word as inputs, determine whether the word can be constructed in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are horizontally or vertically neighbouring. The same letter cell may not be used more than once.

### Example:
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
```

Given word = "ABCCED", return true.

Given word = "SEE", return true.

Given word = "ABCB", return false.


### Input:
1) `board` - 2D array of characters
2) `word` - String word that you are looking for in the board

Assume inputs are separated by spaces and new lines. So for Team A it will look like:
```
A B C E
S F C S
A D E E
```
word



### Output:
Boolean value representing whether the word can be found (true) in the board or not (false). Your function should return this value.
