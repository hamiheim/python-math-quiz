# Python based Math Quiz
## Description
Designed as an alternative to printing out worksheets or do quizzes online, I wrote this quiz to help my son improve his math skills. Supports the ability to select different types of operators (addition, subtraction, etc.) to include the ability for a mixed exam of all for operators.

## Features
A quiz that generates a set number of randomly generated questions that features a score and grade based approach as well as timing the user to show improvement over time. 

### Questions
Allows the user to select from a set number of questions (25, 50, or 100). There is a hidden option for 5 used for testing that can be commented out. Depending on the exam type, the selected number of questions will be generated using a randomly generated set of numbers. At the conclusion of the quiz, it will present the user with the number of correct vs. incorrect questions answered, as well as prompt the user if they'd like to view the questions they got wrong.

#### Addition
Questions use randomly generated numbers ranging between 0 and 999.

#### Subtraction
Questions use randomly generated numbers ranging between 0 and 999.

#### Multiplication
Questions use randomly generated numbers; numerator ranging between 0 and 999 and denominator ranging between 0 and 99.

#### Division
In order to prevent questions with quotients that result in floating numbers, a set of numerators and denominators have been generated in two lists for each product family from 2 through 12. The two lists align to allow for a question with a whole number for the quotient. For example, for the 12 product family, there is a numerator list `nume12` and a denominators list `denom12`. `nume12` has values of exact products of 12, starting at 12, through 144; `denom12` has values of the corresponding product of the value from the `nume12` list, starting at 1, through 12. Questions use a randomly selected index from a randomly selected list.

### Timing
At the conclusion of the test will show the user the total time spent on the test, as well as the average time spent per question. Currently does not specifically record the time spent per questions, but simply average the total time by the number of questions answered.

### Grading
At the conclusion of the test, the user will presented with an overall grade based on the number of correct vs. incorrect answers.

### Scoring
To help improve engagement with the user, the quiz scores the user based on the number of questions answered correctly, as well as the average time spent on each questions. keeps track of a high score for the user to prompt them to continue to test themselves and improve. Scoring is based on the following values:

- Starting value of 0
- 10 points for each correct answer
- Bonus points based on the time spent per question

To motivate the user to improve their score, the quiz will record a high score, and will print out the current score and their current high score at the end of each completed quiz.

#### Bonus points values
Bonus points are awarded using the following metrics:

**Assuming user has completed the test with a grade of 80% or more:**
1. Add 100% of max possible score if average time per question was  less than 5 seconds
2. Add 50% of max possible score if average time was greater than or equal to 5 seconds but less than 10 seconds
3. Add 25% of max possible score if the average time was greater than or equal to 10 seconds but less than 15 seconds

For example, if doing a 25 question quiz, the max score the user could receive is 250 points. If the user gets an 80% or more on the quiz, and the average time spent per question was less than 5 seconds, they will automatically receive a bonux of 250 points. If the average time was 5 - 9 seconds, they receive 125 points, and if it was 10 - 14 seconds, they receive 75 points. If the time was 15 seconds or more, no bonus is awarded. If doing a 100 question quiz the less than 5 second bonus is 1000 points. 


## Installation
Installation is as simple as placing the python file onto a machine with python3 installed and running from a console/terminal. A future version of this quiz is intended to develop an actual program with a GUI interface for the user to interact with.
