# Instructions

Mecha Munch™, a grocery shopping automation company, has just hired you to work on their ordering app. Your team is tasked with building an MVP (minimum viable product) that manages all the basic shopping cart activities, allowing users to add, remove, and sort their grocery orders. Thankfully, a different team is handling all the money and check-out functions!

## Task 1

### Add Item(s) to the User's Shopping Cart

The MVP should allow the user to add items to their shopping cart. This could be a single item or multiple items at once. Since this is an MVP, item quantity is indicated by repeats. If a user wants to add 2 Oranges, 'Oranges' will appear twice in the input iterable. If the user already has the item in their cart, the cart quantity should be increased by 1. If the item is new to the cart, it should be added with a quantity of 1.

Create the function **add_item(<current_cart>, <items_to_add>)** that takes a cart dictionary and any list-like iterable of items to add as arguments. It should return a new/updated shopping cart dictionary for the user.

    >>> add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
                  ('Apple', 'Apple', 'Orange', 'Apple', 'Banana'))
    {'Banana': 4, 'Apple': 5, 'Orange': 2}

    >>> add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
                  ['Banana', 'Orange', 'Blueberries', 'Banana'])
    {'Banana': 5, 'Apple': 2, 'Orange': 2, 'Blueberries': 1}
