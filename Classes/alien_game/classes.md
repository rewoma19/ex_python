# Instructions

Ellen is making a game where the player has to fight aliens. She has just learned about Object Oriented Programming (OOP) and is eager to take advantage of what using **classes** could offer her program.

To Ellen's delight, you have offered to help and she has given you the task of programming the aliens that the player has to fight.

## Task 1

### Create the Alien Class

Define the Alien class with a constructor that accepts two parameters **<x_coordinate>** and **<y_coordinate>**, putting them into **x_coordinate** and **y_coordinate** instance variables. Every alien will also start off with a health level of 3, so the **health** variable should be initialized as well.

    >>> alien = Alien(2, 0)
    >>> alien.x_coordinate
    2
    >>> alien.y_coordinate
    0
    >>> alien.health
    3

Now, each alien should be able to internally track its own position and health.
