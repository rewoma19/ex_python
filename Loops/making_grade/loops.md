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

## Task 3

### The "Best"

The teacher you're assisting wants to find the group of students who've performed "the best" on this exam. What qualifies as "the best" fluctuates, so you need to find the student scores that are greater than or equal to the current threshold.

Create the function **above_threshold(student_scores, threshold)** taking **student_scores** (a **list** of grades), and **threshold** (the "top score" threshold) as parameters. This function should return a **list** of all scores that are **>=** to **threshold**.

    >>> above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
    [90,75,83,96]

## Task 4

### Calculating Letter Grades

Introduction
Python has two looping constructs. while loops for indefinite (uncounted) iteration and for loops for definite, (counted) iteration. The keywords break, continue, and else help customize loop behavior. range() and enumerate() help with loop counting and indexing.

While
while loops will continue to execute as long as the loop expression or "test" evaluates to True in a boolean context, terminating when it evaluates to False:

# Lists are considered "truthy" in a boolean context if they

# contain one or more values, and "falsy" if they are empty.

> > > placeholders = ["spam", "ham", "eggs", "green_spam", "green_ham", "green_eggs"]

> > > while placeholders:
> > > ... print(placeholders.pop(0))
> > > ...
> > > 'spam'
> > > 'ham'
> > > 'eggs'
> > > 'green_spam'
> > > 'green_ham'
> > > 'green_eggs'
> > > For
> > > The basic for loop in Python is better described as a for each which cycles through the values of any iterable object, terminating when there are no values returned from calling next():

> > > word_list = ["bird", "chicken", "barrel", "bongo"]

> > > for word in word_list:
> > > ... if word.startswith("b"):
> > > ... print(f"{word.title()} starts with a B.")
> > > ... else:
> > > ... print(f"{word.title()} doesn't start with a B.")
> > > ...
> > > 'Bird starts with a B.'
> > > 'Chicken doesn\'t start with a B.'
> > > 'Barrel starts with a B.'
> > > 'Bongo starts with a B.'
> > > Sequence Object range()
> > > When there isn't a specific iterable given, the special range() sequence is used as a loop counter. range() requires an int before which to stop the sequence, and can optionally take start and step parameters. If no start number is provided, the sequence will begin with 0. range() objects are lazy (values are generated on request), support all common sequence operations, and take up a fixed amount of memory, no matter how long the sequence specified.

# Here we use range to produce some numbers, rather than creating a list of them in memory.

# The values will start with 1 and stop _before_ 7

> > > for number in range(1, 7):
> > > ... if number % 2 == 0:
> > > ... print(f"{number} is even.")
> > > ... else:
> > > ... print(f"{number} is odd.")
> > > '1 is odd.'
> > > '2 is even.'
> > > '3 is odd.'
> > > '4 is even.'
> > > '5 is odd.'
> > > '6 is even.'

# range() can also take a _step_ parameter.

# Here we use range to produce only the "odd" numbers, starting with 3 and stopping _before_ 15.

> > > for number in range(3, 15, 2):
> > > ... if number % 2 == 0:
> > > ... print(f"{number} is even.")
> > > ... else:
> > > ... print(f"{number} is odd.")
> > > ...
> > > '3 is odd.'
> > > '5 is odd.'
> > > '7 is odd.'
> > > '9 is odd.'
> > > '11 is odd.'
> > > '13 is odd.'
> > > Values and Indexes with enumerate()
> > > If both values and their indexes are needed, the built-in enumerate(<iterable>) will return (index, value) pairs:

> > > word_list = ["bird", "chicken", "barrel", "apple"]

# _index_ and _word_ are the loop variables.

# Loop variables can be any valid python name.

> > > for index, word in enumerate(word_list):
> > > ... if word.startswith("b"):
> > > ... print(f"{word.title()} (at index {index}) starts with a B.")
> > > ... else:
> > > ... print(f"{word.title()} (at index {index}) doesn't start with a B.")
> > > ...
> > > 'Bird (at index 0) starts with a B.'
> > > 'Chicken (at index 1) doesn\'t start with a B.'
> > > 'Barrel (at index 2) starts with a B.'
> > > 'Apple (at index 3) doesn\'t start with a B.'

# The same method can be used as a "lookup" for pairing items between two lists.

# Of course, if the lengths or indexes don't line up, this doesn't work.

> > > word_list = ["cat", "chicken", "barrel", "apple", "spinach"]
> > > category_list = ["mammal", "bird", "thing", "fruit", "vegetable"]

> > > for index, word in enumerate(word_list):
> > > ... print(f"{word.title()} is in category: {category_list[index]}.")
> > > ...
> > > 'Cat is in category: mammal.'
> > > 'Chicken is in category: bird.'
> > > 'Barrel is in category: thing.'
> > > 'Apple is in category: fruit.'
> > > 'Spinach is in category: vegetable.'
> > > Altering Loop Behavior
> > > The continue keyword can be used to skip forward to the next iteration cycle:

word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple", "bear"]

# This will skip _bird_, at index 0

for index, word in enumerate(word_list):
if index == 0:
continue
if word.startswith("b"):
print(f"{word.title()} (at index {index}) starts with a b.")

'Barrel (at index 2) starts with a b.'
'Bongo (at index 3) starts with a b.'
'Bear (at index 6) starts with a b.'
The break (like in many C-related languages) keyword can be used to stop the iteration and "break out" of the innermost enclosing loop:

> > > word_list = ["bird", "chicken", "barrel", "bongo", "sliver", "apple"]

> > > for index, word in enumerate(word_list):
> > > ... if word.startswith("b"):
> > > ... print(f"{word.title()} (at index {index}) starts with a B.")
> > > ... elif word == "sliver":
> > > ... break
> > > ... else:
> > > ... print(f"{word.title()} doesn't start with a B.")
> > > ... print("loop broken.")
> > > ...
> > > 'Bird (at index 0) starts with a B.'
> > > 'Chicken doesn\'t start with a B.'
> > > 'Barrel (at index 2) starts with a B.'
> > > 'Bongo (at index 3) starts with a B.'
> > > 'loop broken.'
> > > Instructions
> > > You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious and mistake-prone. You decide to make things a little more interesting by putting together some functions to count and calculate results for the class.

While you can give "partial credit" on exam questions, overall exam scores have to be ints. So before you can do anything else with the class scores, you need to go through the grades and turn any float scores into ints. Lucky for you, Python has the built-in round() function you can use.

Create the function round_scores(student_scores) that takes a list of student_scores. This function should consume the input list and return a new list with all the scores converted to ints. The order of the scores in the resulting list is not important.

> > > student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
> > > round_scores(student_scores)
> > > ...
> > > [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]

Stuck? Reveal Hints
Opens in a modal
As you were grading the exam, you noticed some students weren't performing as well as you had hoped. But you were distracted, and forgot to note exactly how many students.

Create the function count_failed_students(student_scores) that takes a list of student_scores. This function should count up the number of students who don't have passing scores and return that count as an integer. A student needs a score greater than 40 to achieve a passing grade on the exam.

> > > count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40])
> > > 5

Stuck? Reveal Hints
Opens in a modal
The teacher you're assisting wants to find the group of students who've performed "the best" on this exam. What qualifies as "the best" fluctuates, so you need to find the student scores that are greater than or equal to the current threshold.

Create the function above_threshold(student_scores, threshold) taking student_scores (a list of grades), and threshold (the "top score" threshold) as parameters. This function should return a list of all scores that are >= to threshold.

> > > above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
> > > [90,75,83,96]

Stuck? Reveal Hints
Opens in a modal
The teacher you are assisting likes to assign letter grades as well as numeric scores. Since students rarely score 100 on an exam, the "letter grade" lower thresholds are calculated based on the highest score achieved, and increment evenly between the high score and the failing threshold of <= 40.

Create the function **letter_grades(highest)** that takes the "highest" score on the exam as an argument, and returns a **list** of lower score thresholds for each "American style" grade interval: **["D", "C", "B", "A"]**.

    """Where the highest score is 100, and failing is <= 40.
          "F" <= 40
    41 <= "D" <= 55
    56 <= "C" <= 70
    71 <= "B" <= 85
    86 <= "A" <= 100
    """

    >>> letter_grades(highest=100)
    [41, 56, 71, 86]


    """Where the highest score is 88, and failing is <= 40.
          "F" <= 40
    41 <= "D" <= 52
    53 <= "C" <= 64
    65 <= "B" <= 76
    77 <= "A" <= 88
    """

    >>> letter_grades(highest=88)
    [41, 53, 65, 77]

## Task 5

### Matching Names to Scores

You have a list of exam scores in descending order, and another list of student names also sorted in descending order by their exam scores. You would like to match each student name with their exam score and print out an overall class ranking.

Create the function **student_ranking(student_scores, student_names)** with parameters **student_scores** and **student_names**. Match each student name on the student_names **list** with their score from the student_scores **list**. You can assume each argument list will be sorted from highest score(er) to lowest score(er). The function should return a **list** of strings with the format **<rank>. <student name>: <student score>**
.

    >>> student_scores = [100, 99, 90, 84, 66, 53, 47]
    >>> student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
    >>> student_ranking(student_scores, student_names)
    ...
    ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']

## Task 6

### A "Perfect" Score

xAlthough a "perfect" score of 100 is rare on an exam, it is interesting to know if at least one student has achieved it.

Create the function **perfect_score(student_info)** with parameter **student_info**. **student_info** is a **list** of lists containing the name and score of each student: **[["Charles", 90], ["Tony", 80]]**. The function should **return** the first **[<name>, <score>]** pair of the student who scored 100 on the exam.

If no 100 scores are found in **student_info**, an empty list **[]** should be returned.

    >>> perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
    ["Alex", 100]

    >>> perfect_score(student_info=[["Charles", 90], ["Tony", 80]])
    []
