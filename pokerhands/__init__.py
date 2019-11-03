from collections import namedtuple

from .constants import constants

Card = namedtuple("Card", "rank suit")

def classify(hand):
    """
    Classifies and sorts hand

    Determines hand type and sorts hand in ranking by poker rules
    ex. "2H 3D 4C 5D 6H" will return (constants.hands.STRAIGHT, 6, 5, 4, 3, 2)

    Parameters
    ----------
    hand : tuple
        contains 5 cards

    Returns
    -------
    tuple
        [0] is hand type, [1:6] is hand sorted in decending value order depending on type
    """

    raise NotImplementedError()

def compare(hand1, hand2):
    """
    Compares hand1 to hand2

    Compares its two arguments for order. Returns a negative integer, zero, or a positive integer as the first argument is less than, equal to, or greater than the second.

    In the foregoing description, the notation sgn(expression) designates the mathematical signum function, which is defined to return one of -1, 0, or 1 according to whether the value of expression is negative, zero or positive.

    Parameters
    ----------
    hand1 : tuple
        contains 5 cards

    hand2 : tuple
        contains 5 cards

    Returns
    -------
    -1
        hand1 < hand2
    0
        hand1 == hand2
    1
        hand1 > hand2

    """
    class1 = classify(hand1)
    class2 = classify(hand2)

    for i in range(len(class1)):
        if class1[i] > class2[i]:
            return 1
        elif class1[i] < class2[i]:
            return -1

    return 0

def parse_hands(line):
    """
    Parse poker hands from text line

    Parameters
    ----------
    line : str
        Line containing 2 poker hands (10 groups of 2 chars each)

    Returns
    -------
    tuple, tuple
        hand1 and hand2 of the line
            
    """
    def unmarshal_hand(cards):
        return tuple([Card(c[0],c[1]) for c in cards])

    cards = line.split()
    return unmarshal_hand(cards[0:5]), unmarshal_hand(cards[5:10])

def read(fstr):
    """
    Read poker hands from file

    Parameters
    ----------
    fstr : str
        The file location of the poker hands

    Yields
    -------
    Tuple, Tuple
        hand1 and hand2 of each line
            
    """
    with open(fstr) as f:
        for line in f:
            yield parse_hands(line)