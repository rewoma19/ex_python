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

## Task 2

### The hit Method

Ellen would like the Alien **class** to have a **hit** method that decrements the health of an alien object by 1 when called. This way, she can simply call **<alien>.hit()** instead of having to manually change an alien's health. It is up to you if **hit()** takes healths points to or below zero.

    >>> alien = Alien(0, 0)

    # Initialized health value.
    >>> alien.health
    3

    # Decrements health by 1 point.
    >>> alien.hit()
    >>> alien.health
    2

## Task 3

### The is_alive Method

You realize that if the health keeps decreasing, at some point it will probably hit 0 (or even less!). It would be a good idea to add an **is_alive** method that Ellen can quickly call to check if the alien is... well... alive. 😉 **<alien>.is_alive()** should return a boolean.

    >>> alien.health
    1
    >>> alien.is_alive()
    True
    >>> alien.hit()
    >>> alien.health
    0
    >>> alien.is_alive()
    False

## Task 4

### The teleport Method

In Ellen's game, the aliens have the ability to teleport! You will need to write a **teleport** method that takes new **x_coordinate** and **y_coordinate** values, and changes the alien's coordinates accordingly.

    >>> alien.teleport(5, -4)
    >>> alien.x_coordinate
    5
    >>> alien.y_coordinate
    -4
