# Instructions

Your friend Linus is a Locomotive Engineer who drives cargo trains between cities. Although they are amazing at handling trains, they are not amazing at handling logistics or computers. They would like to enlist your programming help organizing train details and correcting mistakes in route data.

    Note

    This exercise could easily be solved using slicing, indexing, and various dict methods. However, we would like you to practice packing, unpacking, and multiple assignment in solving each of the tasks below.

## Task 1

### Create a list of all wagons

Your friend has been keeping track of each wagon identifier (ID), but they are never sure how many wagons the system is going to have to process at any given time. It would be much easier for the rest of the logistics program to have this data packaged into a unified **list**.

Implement a function **get_list_of_wagons()** that accepts an arbitrary number of wagon IDs. Each ID will be a positive integer. The function should then return the given IDs as a single **list**.

    >>> get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)
    [1, 7, 12, 3, 14, 8, 5]

## Task 2

### Fix the list of wagons

At this point, you are starting to get a feel for the data and how it's used in the logistics program. The ID system always assigns the locomotive an ID of **1**, with the remainder of the wagons in the train assigned a randomly chosen ID greater than **1**.

Your friend had to connect two new wagons to the train and forgot to update the system! Now, the first two wagons in the train **list** have to be moved to the end, or everything will be out of order.

To make matters more complicated, your friend just uncovered a second **list** that appears to contain missing wagon IDs. All they can remember is that once the new wagons are moved, the IDs from this second **list** should be placed directly after the designated locomotive.

Linus would be really grateful to you for fixing their mistakes and consolidating the data.

Implement a function **fix_list_of_wagons()** that takes two **lists** containing wagon IDs. It should reposition the first two items of the first **list** to the end, and insert the values from the second **list** behind (on the right hand side of) the locomotive ID (1). The function should then **return** a **list** with the modifications.

    >>> fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
    [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
