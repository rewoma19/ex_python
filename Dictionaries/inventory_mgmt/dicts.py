"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    Parameters:
        items (list): Items to create an inventory from.

    Returns:
        dict: The inventory dictionary.
    """

    inventory_dict = dict()

    for item in items:
        inventory_dict[item] = items.count(item)

    return inventory_dict
