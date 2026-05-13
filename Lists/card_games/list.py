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

    for index, num in enumerate(nums_list):
        nums_list[index] += index

    return nums_list

print(get_rounds(27))

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

print(concatenate_rounds([27, 28, 29], [35, 36]))

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds  (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    contains_round = number in rounds
    return contains_round

print(list_contains_round([27, 28, 29, 35, 36], 29))
print(list_contains_round([27, 28, 29, 35, 36], 30))

def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """

    card_avg = sum(hand) / len(hand)
    return card_avg

print(card_average([5, 6, 7]))

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    actual_avg = card_average(hand)
    avg_first_last = (hand[0] + hand[-1]) / 2
    middle_index = len(hand) // 2
    avg_median = hand[middle_index]

    return actual_avg in (avg_first_last, avg_median)

print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even_indexed_list = []
    odd_indexed_list = []

    for index, card in enumerate(hand):
        if (index % 2) == 0:
            even_indexed_list.append(card)
        else:
            odd_indexed_list.append(card)

    even_avg = sum(even_indexed_list) / len(even_indexed_list)
    odd_avg = sum(odd_indexed_list) / len(odd_indexed_list)

    return even_avg == odd_avg

print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] *= 2

    return hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))