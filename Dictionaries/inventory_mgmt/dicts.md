# Instructions

In this exercise, you will be managing an inventory system.

The inventory should be organized by the item name and it should keep track of the number of items available.

You will have to handle adding items to an inventory. Each time an item appears in a given list, the item's quantity should be increased by **1** in the inventory. You will also have to handle deleting items from an inventory by decreasing quantities by **1** when requested.

Finally, you will need to implement a function that will return all the key-value pairs in a given inventory as a **list** of **tuples**.

## Task 1

### Create an inventory based on a list

Implement the **create_inventory(<input list>)** function that creates an "inventory" from an input list of items. It should return a **dict** containing each item name paired with their respective quantity.

    >>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
    {"coal":1, "wood":2, "diamond":3}
