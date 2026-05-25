"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    loco_index = each_wagons_id.index(1) # will be 2nd postion
    rest = each_wagons_id[loco_index+1:]
    first_wagon, second_wagon, *others = each_wagons_id
    fixed_list = [1, *missing_wagons, *rest, first_wagon, second_wagon]

    return fixed_list
