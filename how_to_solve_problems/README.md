### Problem 1:

Given your birthday and the current date, calculate your age in days. Assume that the birthday and the current date are correct dates (and no time travel). Simply put, if you were born 1 Jan 2012 and todays date is 2 Jan 2012 you are one day old

# How to solve problems

What is the first thing we do when we approach a problem?
ans: Make sure we understand the problem

## Understanding a problem.

Problem is defined by possible inputs and the relationships between the inputs and the output.
A solution is any procedure that can take the inputs and give the desired output that the problem dictates or the relationship we want

#### Rules to solving problems

- What are the inputs?
  "Given your birthday and the current date, calculate your age in days"
  inputs = your birthday and current date

  - What is the set of valid inputs?

    - Second date must nut be more than first date
    - Dates must be valid in Gregorian calendar (15 Oct 1582)

  - How are inputs represented?

    ```python
        def day_between_dates(year_1, month_1, day_1,year_2, month_2, day_2):
    ```

- What are the outputs?
  ans: return a number given the number of days between the first date and the second date.

- Solve the problem, Work through some examples by hand.

Problem statement: Define a procedure, days_between_dates, that takes the dates as input and returns the number of days between the first date and the second date. Each date is passed in as three numbers giving a valid year, month, and day in the Gregorian calendar. The second date must not be before the first.

    - Write out the expected output for some inputs and work it manually

    - Consider, systematically, how a human would solve the problem.
    e.g: daysBetweenDates(2013,1,24,2013,6,29):

    Look at a calendar and count the days between Jan 24 to June 29th.

- Simple mechanical solution.

### Algorithm pseudocode

###### first iteration

    days = number of days in month 1 - day_1
    month_1 += 1
    while month_1 < month_2:
        days += number of days in month_1
        month_1 += 1
    days += day_2
    while year_1 < year_2:
        days += numnber of days in year_1

    above doesnt handle:
    - input dates in the same month
    - month_2 < month_1 and year_2 > year_1
    - days in leap years

###### second iteration

    days = 0
    while date_1 is before date_2:
        date_1 =  advance to next day
        days += 1
