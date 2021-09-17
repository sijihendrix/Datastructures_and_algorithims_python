### Exercise 1: In the following exercise you will finish writing smallest_positive which is a function that finds the smallest positive number in a list.

### Exercise 2: Now let's assume you are planning on taking some additional courses at your local educational institution, and you have acquired some data about the available courses and when they will be offered. In the following exercise, you will write control structures to process the data and return the semesters when a given course is offered.

You will need to complete the function when_offered(courses, course). This function accepts a "courses" data structure and a "course" string. The function should return a list of strings representing the semesters when the input course is offered. See the two test cases below for examples of correct results.

Since the when_offered function accepts a dictionary data structure, you will find the construct useful, as this loops through the key values in a dictionary.

```python
 for <key> in <dictionary>:
    <block>
```

# Function and Generator Practice

### Exercise 1

#### In the following exercise, you will create a generator fact_gen() that generates factorials. For a number n, n factorial is denoted by n!, and it is the product of all positive integers less than or equal to n. For example,

5! = 5 _ 4 _ 3 _ 2 _ 1 = 120

In this exercise, you will define prod(a, b) which returns the product of numbers a and b. You will also define fact_gen() which yields the next factorial number.

### Exercise 2

In the next exercise, you will write a function that checks sudoku squares for correctness.

Sudoku is a logic puzzle where a game is defined by a partially filled 9 x 9 square of digits where each square contains one of the digits 1, 2, 3, 4, 5, 6, 7, 8, 9. For this question we will generalize and simplify the game.

Define a procedure, check_sudoku, that takes as input a square list of lists representing an n x n sudoku puzzle solution and returns the boolean True if the input is a valid sudoku square and returns the boolean False otherwise.

A valid sudoku square satisfies these two properties:

Each column of the square contains each of the whole numbers from 1 to n exactly once.

Each row of the square contains each of the whole numbers from 1 to n exactly once.

You may assume that the input is square and contains at least one row and column.

# Python Class Practice

## Exercise 1

Now let's assume that the current month is April, and you want to use a Person class to help make use of information about the friends in your contacts list. In particular, you'd like to increment the age of all of your friends with birthdays in April. You would also like to know who they are, along with their current ages, so you can send them birthday cards. Finally, you would also like to figure out which month has the most friends with birthdays, so you can budget for all of the birthday cards you will need to buy.

In the following exercise, the Person class will be provided for you, and you will be working with a list of instances of the class, representing friends in your contacts. This list is stored in the variable people.

To complete the exercise, you will need to do two things:

Complete the function get_april_birthdays(people). This function should return a dictionary with each name of your friend with an April birthday as a key, and their updated age as the value.
Complete the function get_most_common_month(people). This function should return the name of the month with the most number of birthdays among your friends.
There is some testing code provided in test(), and there are more specific TODO instructions in each of the two functions mentioned.
