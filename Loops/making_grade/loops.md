# Instructions

You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious and mistake-prone. You decide to make things a little more interesting by putting together some functions to count and calculate results for the class.

## Task 1

### Rounding Scores

While you can give "partial credit" on exam questions, overall exam scores have to be **int**s. So before you can do anything else with the class scores, you need to go through the grades and turn any **float** scores into **int**s. Lucky for you, Python has the built-in **round()** function you can use.

Create the function **round_scores(student_scores)** that takes a **list** of **student_scores**. This function should consume the input **list** and **return** a new list with all the scores converted to **int**s. The order of the scores in the resulting **list** is not important.

    >>> student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
    >>> round_scores(student_scores)
    ...
    [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]

## Task 2

### Non-Passing Students

As you were grading the exam, you noticed some students weren't performing as well as you had hoped. But you were distracted, and forgot to note exactly how many students.

Create the function **count_failed_students(student_scores)** that takes a **list** of **student_scores**. This function should count up the number of students who don't have passing scores and return that count as an integer. A student needs a score greater than 40 to achieve a passing grade on the exam.

    >>> count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40])
    5
