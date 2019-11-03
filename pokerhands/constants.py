from collections import namedtuple

def const(c):
    for k,v in c.items():
        if isinstance(v, dict):
            c[k] = const(v)

    return namedtuple("Const", c.keys())(*c.values())

constants = const({
    "ranks" : {
        "TEN": 10,
        "JACK":11,
        "QUEEN":12,
        "KING":13,
        "ACE":14
    },
    "hands": {
        "HIGH_CARD": 0,
        "ONE_PAIR": 1,
        "TWO_PAIR": 2,
        "THREE_OF_A_KIND": 3,
        "STRAIGHT": 4,
        "FLUSH": 5,
        "FULL_HOUSE": 6,
        "FOUR_OF_A_KING": 7,
        "STRAIGHT_FLUSH": 8,
        "ROYAL_FLUSH": 9
    }
})