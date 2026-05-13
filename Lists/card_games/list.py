"""Functions for tracking poker hands and assorted card tasks.
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int):  The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    nums_list = [number] * 3

    for i in range(len(nums_list)):
        nums_list[i] += i

    return nums_list

get_rounds(27)

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list):  The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """

    rounds_1.extend(rounds_2)
    return rounds_1

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds  (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return (number in rounds)
