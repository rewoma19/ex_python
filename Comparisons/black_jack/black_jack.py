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