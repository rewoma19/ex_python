"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int:  The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    card_val = 0

    if card == "A":
        card_val = 1
    elif card in "JQK":
        card_val = 10
    else:
        card_val = int(card)

    return card_val

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting Tuple contains both cards if they are of equal value.
    """

    card_one_val = value_of_card(card_one)
    card_two_val = value_of_card(card_two)

    higher_card = card_one

    if card_one_val == card_two_val:
        higher_card = (card_one, card_two)
    elif card_one_val < card_two_val:
        higher_card = card_two

    return higher_card