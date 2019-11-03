from collections import namedtuple, defaultdict, deque

from .constants import constants

Card = namedtuple("Card", "rank suit")

def rank(card):
    """
    Ranks a card numerically

    Parameters
    ----------
    card : Card
        contains a rank and a suit member

    Returns
    -------
    integer
        numeric rank of a card given its string rank
    """
    if '1' <= card.rank <= '9':
        return ord(card.rank) - ord('0')

    return {
        "T": constants.ranks.TEN,
        "J": constants.ranks.JACK,
        "Q": constants.ranks.QUEEN,
        "K": constants.ranks.KING,
        "A": constants.ranks.ACE       
    }[card.rank]

def ranked(hand):
    """
    Maps rank function to hand

    Parameters
    ----------
    hand : tuple
        contains 5 cards

    Returns
    -------
    list
        map of rank() to hand
    """

    return [rank(c) for c in hand]

def bucket_sort(hand):
    """
    Sorts cards in a hand into rank buckets

    Parameters
    ----------
    hand : tuple
        contains 5 cards

    Returns
    -------
    dict
        A dictionary mapping rank to list of cards
    """

    buckets = defaultdict(list)

    for card in hand:
        buckets[rank(card)].append(card)

    return buckets

def max_bucket_len(buckets):
    """
    Finds the maximum length of a bucket in buckets (dict as returned by bucket_sort)

    Parameters
    ----------
    buckets : dict
        contains a map of ranks to list of cards

    Returns
    -------
    integer
        length of the longest bucket in buckets
    """
    m = 1
    for k,v in buckets.items():
        m = max(m, len(v))

    return m

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
    def ordered(hand):
        return list(sorted(ranked(hand), reverse=True))

    def ordered_four_of_a_kind(hand):
        d = deque()

        for rank,bucket in bucket_sort(hand).items():
            if len(bucket) == 4:
                d.extendleft(ranked(bucket))
            else:
                d.extend(ranked(bucket))

        return list(d)

    def ordered_full_house(hand):
        d = deque()

        for rank,bucket in bucket_sort(hand).items():
            if len(bucket) == 3:
                d.extendleft(ranked(bucket))
            else:
                d.extend(ranked(bucket))

        return list(d)

    def ordered_three_of_a_kind(hand):
        d = deque()
        others = list()

        for rank,bucket in bucket_sort(hand).items():
            if len(bucket) == 3:
                d.extendleft(ranked(bucket))
            else:
                others.extend(bucket)

        d.extend(ordered(others))

        return list(d)

    def ordered_two_pair(hand):
        d = deque()
        outsider = None

        for rank,bucket in bucket_sort(hand).items():
            if len(bucket) == 2:
                d.extendleft(ranked(bucket))
            else:
                outsider = rank

        d = sorted(d, reverse=True)
        d.append(outsider)

        return list(d)

    def ordered_one_pair(hand):
        d = deque()
        others = list()

        for rank,bucket in bucket_sort(hand).items():
            if len(bucket) == 2:
                d.extendleft(ranked(bucket))
            else:
                others.extend(bucket)

        d.extend(ordered(others))

        return list(d)

    def is_one_pair(hand):
        buckets = bucket_sort(hand)
        return len(buckets.keys()) == 4

    def is_two_pair(hand):
        buckets = bucket_sort(hand)

        return len(buckets.keys()) == 3 and max_bucket_len(buckets) == 2

    def is_three_of_a_kind(hand):
        buckets = bucket_sort(hand)

        m = 1
        for k,v in buckets.items():
            m = max(m, len(v))

        return len(buckets.keys()) == 3 and max_bucket_len(buckets) == 3

    def is_straight(hand):
        l = sorted(ranked(hand))

        for i in range(1, len(l)):
            if l[i] - l[i-1] != 1: return False

        return True

    def is_flush(hand):
        s = hand[0].suit

        for card in hand[1:]:
            if card.suit != s: return False

        return True

    def is_full_house(hand):
        buckets = bucket_sort(hand)
        return len(buckets.keys()) == 2 and max_bucket_len(buckets) == 3

    def is_four_of_a_kind(hand):
        buckets = bucket_sort(hand)
        return len(buckets.keys()) == 2 and max_bucket_len(buckets) == 4

    def is_straight_flush(hand):
        return is_straight(hand) and is_flush(hand)

    def is_royal_flush(hand):
        return is_straight_flush(hand) and constants.ranks.ACE in ranked(hand)

    if is_royal_flush(hand):
        return tuple([constants.hands.ROYAL_FLUSH] + ordered(hand))
    elif is_straight_flush(hand):
        return tuple([constants.hands.STRAIGHT_FLUSH] + ordered(hand))
    elif is_four_of_a_kind(hand):
        return tuple([constants.hands.FOUR_OF_A_KIND] + ordered_four_of_a_kind(hand))
    elif is_full_house(hand):
        return tuple([constants.hands.FULL_HOUSE] + ordered_full_house(hand))
    elif is_flush(hand):
        return tuple([constants.hands.FLUSH] + ordered(hand))
    elif is_straight(hand):
        return tuple([constants.hands.STRAIGHT] + ordered(hand))
    elif is_three_of_a_kind(hand):
        return tuple([constants.hands.THREE_OF_A_KIND] + ordered_three_of_a_kind(hand))
    elif is_two_pair(hand):
        return tuple([constants.hands.TWO_PAIR] + ordered_two_pair(hand))
    elif is_one_pair(hand):
        return tuple([constants.hands.ONE_PAIR] + ordered_one_pair(hand))
    else:
        return tuple([constants.hands.HIGH_CARD] + ordered(hand))

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