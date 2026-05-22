"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for new_item in set(items_to_add):
        item_count = items_to_add.count(new_item)
        if new_item not in current_cart:
            current_cart[new_item] = item_count
        else:
            current_cart[new_item] += item_count

    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    user_cart = dict.fromkeys(notes, 1)

    return user_cart

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)

    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    sorted_cart = sorted(cart.items())
    return dict(sorted_cart)

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}

    for item, qty in cart.items():
        aisle, refridge = aisle_mapping[item]
        fulfillment_cart[item] = [qty, aisle, refridge]

    cart_items = fulfillment_cart.items()
    sorted_cart = dict(sorted(cart_items, reverse= True))

    return sorted_cart

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item, (inventory_qty, *rest) in store_inventory.items():
        if item in fulfillment_cart:
          cart_qty = fulfillment_cart[item][0]

          if (inventory_qty - cart_qty) > 0:
            store_inventory[item][0] = inventory_qty - cart_qty
          else:
              store_inventory[item][0] = "Out of Stock"

    return store_inventory
